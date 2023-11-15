# Testy - Zadanie 4
import unittest
from lab6_4 import count_letters, group_words_by_first_letter

class TestLab59(unittest.TestCase):

    def test_count_letters(self):
        self.assertEqual(count_letters('aaaaa'), {'a': 5})
        self.assertEqual(count_letters('abbccaaaa'), {'a': 5, 'b': 2, 'c': 2})
        self.assertEqual(count_letters('abc'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(count_letters(''), {})
        self.assertEqual(count_letters('aAaAa'), {'a': 3, 'A': 2})

    def test_group_words_by_first_letter(self):
        self.assertEqual(group_words_by_first_letter("ala ma kota"), {'a': ['ala'], 'm': ['ma'], 'k': ['kota']})
        self.assertEqual(group_words_by_first_letter("ala ma kota ala ma psa"), {'a': ['ala', 'ala'], 'm': ['ma', 'ma'], 'k': ['kota'], 'p': ['psa']})
        self.assertEqual(group_words_by_first_letter("ala ma kota ale marysia ma konia"), {'a': ['ala', 'ale'], 'm': ['ma', 'marysia', 'ma'], 'k': ['kota', 'konia']})
        self.assertEqual(group_words_by_first_letter(""), {})
        self.assertEqual(group_words_by_first_letter("Aa Aa"), {'a': ['Aa', 'Aa']})

if __name__ == '__main__':
    unittest.main()
