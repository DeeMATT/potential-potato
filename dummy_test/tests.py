import unittest

from .views import add_numbers


class TestAddition(unittest.TestCase):

    def test_not_null(self):

        result = add_numbers(10, 5)

        # check if result is None
        self.assertIsNotNone(result)

    def test_int_addition(self):

        result = add_numbers("love", 2)

        # check if result is an integer
        self.assertIsInstance(result, int, "Numbers should be an integer")


if __name__ == '__main__':
    unittest.main()
