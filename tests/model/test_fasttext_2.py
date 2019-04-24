from pathlib import Path
from unittest import TestCase
import fastText

from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData


class TestFastText(TestCase):
    def test_fasttext(self):
        corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.AIVIVN2019_SA)
        hyper_params = {"lr": 0.01,
                        "epoch": 20,
                        "wordNgrams": 3,
                        "dim": 20}
        model = fastText.train_supervised(input="/home/anhv/.languageflow/datasets/aivivn2019_sa/train.txt",
                                          **hyper_params)
        dev_score = model.test("/home/anhv/.languageflow/datasets/aivivn2019_sa/dev.txt")
        test_core = model.test("/home/anhv/.languageflow/datasets/aivivn2019_sa/test.txt")
        print(dev_score)
        print(test_core)
