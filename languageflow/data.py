from typing import List


class Corpus:
    pass


class Sentence:
    pass


class PlaintextCorpus(Corpus):
    def __init__(self, sentences):
        self.sentences = sentences


class CategorizedCorpus(Corpus):
    def __init__(
        self,
        train: List[Sentence],
        dev: List[Sentence],
        test: List[Sentence]
    ):
        self._train: List[Sentence] = train
        self._dev: List[Sentence] = dev
        self._test: List[Sentence] = test

    @property
    def train(self) -> List[Sentence]:
        return self._train

    @property
    def dev(self) -> List[Sentence]:
        return self._dev

    @property
    def test(self) -> List[Sentence]:
        return self._test


class TaggedCorpus(Corpus):
    pass
