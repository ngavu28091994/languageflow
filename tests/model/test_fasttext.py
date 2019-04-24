from os.path import dirname
from pathlib import Path
from unittest import TestCase
import fastText

from languageflow.data import CategorizedCorpus
from languageflow.data_fetcher import DataFetcher, NLPData


class TestFastText(TestCase):
    def test_fasttext(self):
        # corpus: CategorizedCorpus = DataFetcher.load_corpus(NLPData.AIVIVN2019_SA)
        hyper_params = {"lr": 0.01,
                        "epoch": 20,
                        "wordNgrams": 3,
                        "dim": 20}
        data_folder = Path(dirname(dirname(dirname(__file__)))) / "languageflow" / "data" / "aivivn2019_sa_sample"
        train_file = data_folder / "train.txt"
        dev_file = data_folder / "dev.txt"
        test_file = data_folder / "test.txt"
        model = fastText.train_supervised(input=str(train_file), **hyper_params)
        dev_score = model.test(str(dev_file))
        test_core = model.test(str(test_file))
        print(dev_score)
        print(test_core)
