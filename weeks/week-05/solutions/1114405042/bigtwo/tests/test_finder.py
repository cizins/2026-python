import unittest
from game.models import Card, Hand
from game.finder import HandFinder

class TestFinder(unittest.TestCase):
    def test_find_singles(self):
        h = Hand([Card(3,0), Card(4,1)])
        s = HandFinder.find_singles(h)
        self.assertEqual(len(s), 2)
        
if __name__ == '__main__':
    unittest.main()
