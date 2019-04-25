from typing import List

from languageflow.data import Corpus, Sentence
from languageflow.models.text_classifier import TextClassifier, TEXT_CLASSIFIER_ESTIMATOR
import shutil
import tempfile
from os.path import join
from pathlib import Path
import fastText

from languageflow.transformer.count import CountVectorizer


class ModelTrainer:

    def __init__(self, classifier: TextClassifier, corpus: Corpus):
        self.classifier = classifier
        self.corpus = corpus

    def train(self, model_folder: str):
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

            print(dev_score)
            print(test_core)

        if self.classifier.estimator == TEXT_CLASSIFIER_ESTIMATOR.SVC:
            train_sentences =  self._convert_list_sentences(self.corpus.train)
            dev_sentences = self._convert_list_sentences(self.corpus.dev)
            test_sentences = self._convert_list_sentences(self.corpus.test)
            transformer = CountVectorizer(ngram_range=(1, 2), max_features=4000)

            print(0)

    def _convert_list_sentences(self, sentences: List[Sentence]):
        return [s.text for s in sentences]
