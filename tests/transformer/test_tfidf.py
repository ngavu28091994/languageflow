from unittest import TestCase

from underthesea_flow.transformer.tfidf import TfidfDictionaryVectorizer


class TestTfidfDictionaryVectorizer(TestCase):
    def test_text2vec(self):
        input = u""
        tfidf_dictionary_vecorizer = TfidfDictionaryVectorizer()
        text2vec = tfidf_dictionary_vecorizer.text2vec(input)
        expected = text2vec()
        actual = u""
        self.assertEqual(expected, actual)
