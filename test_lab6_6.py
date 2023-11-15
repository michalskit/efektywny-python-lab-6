import unittest
from lab6_6 import BagOfWords
from io import StringIO

class TestBagOfWords(unittest.TestCase):

    def test_initialization(self):
        # Test initialization with string
        bow = BagOfWords("ala ma kota ala ma ala")
        self.assertEqual(bow.word_counts, {"ala": 3, "ma": 2, "kota": 1})

        # Test initialization with file-like object
        file_like = StringIO("tomek tez ma kota")
        bow_file = BagOfWords(file_like)
        self.assertEqual(bow_file.word_counts, {"tomek": 1, "tez": 1, "ma": 1, "kota": 1})

    def test_string_representation(self):
        bow = BagOfWords("ala ma kota ala ma ala")
        representation = str(bow)
        for word, count in bow.word_counts.items():
            self.assertIn(f"{word}:{count}", representation)

    def test_membership(self):
        bow = BagOfWords("ala ma kota")
        self.assertTrue('ala' in bow)
        self.assertFalse('tomek' in bow)

    def test_iteration_order(self):
        bow = BagOfWords("kota ala ala")
        words = [word for word in bow]
        self.assertEqual(words, ['ala', 'kota'])

    def test_addition(self):
        bow1 = BagOfWords("ala ma kota")
        bow2 = BagOfWords("tomek tez ma")
        bow3 = bow1 + bow2
        expected_counts = {"ala": 1, "ma": 2, "kota": 1, "tomek": 1, "tez": 1}
        for word, count in expected_counts.items():
            self.assertEqual(bow3[word], count)

    def test_item_access_and_update(self):
        bow = BagOfWords("ala ma kota ala ma ala")
        self.assertEqual(bow["ala"], 3)
        bow["tomek"] = 10
        self.assertEqual(bow["tomek"], 10)

if __name__ == '__main__':
    unittest.main()
