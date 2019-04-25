from unittest import TestCase
from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData
from languageflow.models.text_classifier import TextClassifier
from languageflow.trainers.model_trainer import ModelTrainer


class TestFastText(TestCase):
    def test_fasttext(self):
        corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.AIVIVN2019_SA_SAMPLE)
        classifier = TextClassifier()
        model_trainer = ModelTrainer(classifier, corpus)
        model_folder = ""
        model_trainer.train(model_folder)
