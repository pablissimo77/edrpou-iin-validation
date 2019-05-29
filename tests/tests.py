import unittest
from edrpou import valid


class EdrpouTestCase(unittest.TestCase):
    def test_edrpou(self):
        self.assertEqual(valid("3726352025"), (False, "0", "3726352025"))
        self.assertEqual(valid("3726352020"), (True, "0", "3726352020"))


if __name__ == "__main__":
    unittest.main()
