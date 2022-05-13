import unittest
from elephant_counting import combine_lists, combinations

class TestElephantCounting(unittest.TestCase):

    def test_combine_lists(self):
        """given two lists, the output should be a string containing expected letters"""

        s = combine_lists(['a', 'b', 'c'], [1, 0, 0])
        self.assertEqual('a', s)


    def test_combination_generator(self):
        """ Consume the generator a few times and see what happens """

        for combo in combinations('elephant'):
            print(combo)

if __name__ == '__main__':
    unittest.main()
