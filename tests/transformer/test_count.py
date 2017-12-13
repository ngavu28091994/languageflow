from unittest import TestCase

from languageflow.transformer.count import CountVectorizer


class TestCountVectorizer(TestCase):
    def test_tfidf(self):
        text = ["tôi đi học",
                "tôi ăn cơm",
                "cơm rất ngon"]
        vectorizer = CountVectorizer()
        vector = vectorizer.fit_transform(text)
        vocab = vectorizer.vocabulary_
        self.assertGreater(len(vocab), 5)
