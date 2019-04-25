import json
import warnings

# ignore warnings when using transformer
# see: https://github.com/scikit-learn/scikit-learn/issues/12327
warnings.simplefilter("ignore", category=PendingDeprecationWarning)

from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from languageflow.data import Corpus, Sentence
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
import shutil
import tempfile
from os.path import join
from pathlib import Path
import fastText
import joblib

from languageflow.transformer.count import CountVectorizer


class ModelTrainer:

    def __init__(self, classifier: TextClassifier, corpus: Corpus):
        self.classifier = classifier
        self.corpus = corpus

    def train(self, model_folder: str, scoring=f1_score):
        metadata = {"estimator": self.classifier.estimator.value}
        if self.classifier.estimator == TEXT_CLASSIFIER_ESTIMATOR.FAST_TEXT:
            hyper_params = {"lr": 0.01,
                            "epoch": 20,
                            "wordNgrams": 3,
                            "dim": 20}
            tmp_data_folder = tempfile.mkdtemp()

            self.corpus.save(tmp_data_folder)
            train_file = Path(tmp_data_folder) / "train.txt"
            dev_file = Path(tmp_data_folder) / "dev.txt"
            test_file = Path(tmp_data_folder) / "test.txt"
            model = fastText.train_supervised(input=str(train_file), **hyper_params)
            dev_score = model.test(str(dev_file))
            test_core = model.test(str(test_file))
            shutil.rmtree(tmp_data_folder)

            path_to_file = join(model_folder, "model.bin")
            model.save_model(path_to_file)
            print(f"Model is saved in {path_to_file}")

            print("Dev score:", dev_score)
            print("Test score:", test_core)

        if self.classifier.estimator == TEXT_CLASSIFIER_ESTIMATOR.SVC:
            train, dev, test = self._convert_corpus(self.corpus)
            X_train, y_train = train
            X_dev, y_dev = dev
            X_test, y_test = test
            transformer = CountVectorizer(ngram_range=(1, 3), max_features=4000)

            X_train = transformer.fit_transform(X_train)
            joblib.dump(transformer, join(model_folder, "x_transformer.joblib"))

            y_transformer = LabelEncoder()
            y_train = y_transformer.fit_transform(y_train)
            joblib.dump(y_transformer, join(model_folder, "y_transformer.joblib"))

            estimator = SVC(kernel='linear', C=0.3)
            estimator.fit(X_train, y_train)
            joblib.dump(estimator, join(model_folder, "estimator.joblib"))

            X_dev = transformer.transform(X_dev)
            y_dev = y_transformer.transform(y_dev)
            y_dev_pred = estimator.predict(X_dev)
            dev_score = scoring(y_dev, y_dev_pred)

            X_test = transformer.transform(X_test)
            y_test = y_transformer.transform(y_test)
            y_test_pred = estimator.predict(X_test)
            test_core = scoring(y_test, y_test_pred)

            print("Dev score:", dev_score)
            print("Test score:", test_core)
        with open(join(model_folder, "metadata.json"), "w") as f:
            content = json.dumps(metadata, ensure_ascii=False)
            f.write(content)

    def _convert_corpus(self, corpus: Corpus):
        X_train = [s.text for s in corpus.train]
        y_train = [s.labels[0].value for s in corpus.train]

        X_dev = [s.text for s in corpus.dev]
        y_dev = [s.labels[0].value for s in corpus.dev]

        X_test = [s.text for s in corpus.test]
        y_test = [s.labels[0].value for s in corpus.test]
        return (X_train, y_train), (X_dev, y_dev), (X_test, y_test)
