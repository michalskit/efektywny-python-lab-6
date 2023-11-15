# Testy - Zadanie 5
import unittest
from lab6_5 import FrozenDictionary


class TestFrozenDictionary(unittest.TestCase):

    def test_initialization(self):
        """Test whether the FrozenDictionary is initialized correctly."""
        original_dict = {'apple': 5, 'banana': 3}
        frozen_dict = FrozenDictionary(original_dict)
        self.assertEqual(frozen_dict._dict, original_dict)

    def test_hashing(self):
        """Test the hashing of the FrozenDictionary."""
        frozen_dict = FrozenDictionary({'apple': 5, 'banana': 3})
        self.assertIsInstance(hash(frozen_dict), int)

    def test_equality(self):
        """Test equality comparison between two FrozenDictionary instances."""
        dict1 = FrozenDictionary({'apple': 5, 'banana': 3})
        dict2 = FrozenDictionary({'apple': 5, 'banana': 3})
        dict3 = FrozenDictionary({'apple': 4, 'banana': 3})
        self.assertEqual(dict1, dict2)
        self.assertNotEqual(dict1, dict3)

    def test_representation(self):
        """Test the string representation of the FrozenDictionary."""
        frozen_dict = FrozenDictionary({'apple': 5, 'banana': 3})
        self.assertEqual(repr(frozen_dict), "{apple: 5, banana: 3}")

    def test_get_item(self):
        """Test retrieving an item from the FrozenDictionary."""
        frozen_dict = FrozenDictionary({'apple': 5, 'banana': 3})
        self.assertEqual(frozen_dict['apple'], 5)
        self.assertEqual(frozen_dict['banana'], 3)


if __name__ == '__main__':
    unittest.main()
