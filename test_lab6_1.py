# Testy - Zadanie 1
import unittest
from lab6_1 import exercises_completed

class TestExerciseCompletion(unittest.TestCase):
    def test_exercises_completion(self):
        self.assertTrue(exercises_completed)

if __name__ == '__main__':
    unittest.main()
