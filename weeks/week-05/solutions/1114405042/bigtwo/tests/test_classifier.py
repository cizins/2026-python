import unittest
from game.models import Card
from game.classifier import HandClassifier, CardType

class TestClassifier(unittest.TestCase):
    def test_single(self):
        c = HandClassifier.classify([Card(3, 0)])
        self.assertEqual(c[0], CardType.SINGLE)
        
if __name__ == '__main__':
    unittest.main()
