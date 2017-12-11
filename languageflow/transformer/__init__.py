import abc
from abc import ABC


class Transformer(ABC):
    @abc.abstractmethod
    def transform(self):
        pass

    @abc.abstractmethod
    def fit_transform(self):
        pass
