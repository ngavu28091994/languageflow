# -*- coding: utf-8 -*-
from unittest import TestCase

from underthesea_flow.transformer.tagged import TaggedTransformer, sent2labels


class TestTaggedTransformer(TestCase):
    def test_words(self):
        input = "A B , C D"
        tagged = TaggedTransformer()
        expected = tagged.format_word(input)
        actual = ['A\tB_W', 'B\tB_W', ',\tO', 'C\tB_W', 'D\tB_W']
        self.assertEqual(expected, actual)

    def test_words_1(self):
        input = "ông_chủ Nhà_Trắng"
        tagged = TaggedTransformer()
        expected = tagged.format_word(input)
        actual = ['ông\tB_W', 'chủ\tI_W', 'Nhà\tB_W', 'Trắng\tI_W']
        self.assertEqual(expected, actual)

    def test_words_2(self):
        input = "A_B . , C_D ;"
        tagged = TaggedTransformer()
        expected = tagged.format_word(input)
        actual = ['A\tB_W', 'B\tI_W', '.\tO', ',\tO', 'C\tB_W', 'D\tI_W', ';\tO']
        self.assertEqual(expected, actual)

    def test_words_3(self):
        input = "123@mail 456 ;"
        tagged = TaggedTransformer()
        expected = tagged.format_word(input)
        actual = ['123@mail\tB_W', '456\tB_W', ';\tO']
        self.assertEqual(expected, actual)
