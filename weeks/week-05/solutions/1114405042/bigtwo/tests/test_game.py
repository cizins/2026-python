import unittest
from game.game import BigTwoGame

class TestGame(unittest.TestCase):
    def test_setup(self):
        g = BigTwoGame()
        g.setup()
        self.assertEqual(len(g.players), 4)
        for p in g.players:
            self.assertEqual(len(p.hand), 13)
            
if __name__ == '__main__':
    unittest.main()
