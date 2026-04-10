import unittest
from game.models import Card, Hand
from game.ai import AIStrategy

class TestAI(unittest.TestCase):
    def test_score(self):
        h = Hand([Card(3,0)])
        s = AIStrategy.score_play([Card(3,0)], h)
        self.assertTrue(s > 0)
        
if __name__ == '__main__':
    unittest.main()
