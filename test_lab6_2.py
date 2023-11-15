# Testy - Zadanie 2
import unittest


class TestAtomFilter(unittest.TestCase):

    def test_file_comparison(self):
        with open('clean_atoms.txt', 'r') as student_file, open('test_clean_atoms.txt', 'r') as test_file:
            student_content = student_file.read()
            test_content = test_file.read()

        self.assertEqual(student_content, test_content)


if __name__ == '__main__':
    unittest.main()
