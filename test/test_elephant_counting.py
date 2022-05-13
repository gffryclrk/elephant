import unittest
from elephant_counting import combine_lists

class TestElephantCounting(unittest.TestCase):

    def test_combine_lists(self):
        """given two lists, the output should be a string containing expected letters"""

        s = combine_lists(['a', 'b', 'c'], [1, 0, 0])
        self.assertEqual('a', s)


if __name__ == '__main__':
    unittest.main()
