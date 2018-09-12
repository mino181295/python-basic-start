import unittest

class TestBasic(unittest.TestCase):
    """
    Our basic test class
    """

    def test_basic(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        self.assertEqual(1, 1)
        self.assertNotEqual(-100, 100)


if __name__ == '__main__':
    unittest.main()