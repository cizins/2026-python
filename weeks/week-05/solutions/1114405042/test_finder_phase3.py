"""Phase 3 牌型搜尋測試

對應測試目標：HandFinder
預期被測試模組：game/finder.py

執行方式：
python -m unittest test_finder_phase3.py -v
"""

import importlib
import unittest

# 動態匯入，若尚未完成實作可給出明確錯誤訊息。
try:
    models = importlib.import_module("game.models")
    classifier_mod = importlib.import_module("game.classifier")
    finder_mod = importlib.import_module("game.finder")

    Card = models.Card
    Hand = models.Hand
    CardType = classifier_mod.CardType
    HandClassifier = classifier_mod.HandClassifier
    HandFinder = finder_mod.HandFinder
    IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    Card = Hand = CardType = HandClassifier = HandFinder = None
    IMPORT_ERROR = exc


class ImportGuard(unittest.TestCase):
    """共用前置檢查。"""

    def setUp(self):
        if IMPORT_ERROR is not None:
            self.fail(f"無法匯入 game.finder / game.classifier / game.models：{IMPORT_ERROR}")


def _play_signature(play):
    """將一組出牌轉成可比較的簽章（忽略原始順序）。"""
    return tuple(sorted((card.rank, card.suit) for card in play))


class TestFindSingles(ImportGuard):
    def test_find_singles(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        singles = HandFinder.find_singles(hand)

        self.assertEqual(len(singles), 3)
        self.assertTrue(all(len(p) == 1 for p in singles))

        found = {_play_signature(p) for p in singles}
        expect = {
            _play_signature([Card(14, 3)]),
            _play_signature([Card(13, 2)]),
            _play_signature([Card(3, 0)]),
        }
        self.assertEqual(found, expect)

    def test_find_singles_empty(self):
        hand = Hand([])
        self.assertEqual(HandFinder.find_singles(hand), [])


class TestFindPairs(ImportGuard):
    def test_find_pairs_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(HandClassifier.classify(pairs[0])[0], CardType.PAIR)

    def test_find_pairs_two(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        pairs = HandFinder.find_pairs(hand)

        # 應找到 A 對子與 K 對子各一組。
        self.assertEqual(len(pairs), 2)
        ranks = sorted(HandClassifier.classify(p)[1] for p in pairs)
        self.assertEqual(ranks, [13, 14])

    def test_find_pairs_none(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        self.assertEqual(HandFinder.find_pairs(hand), [])


class TestFindTriples(ImportGuard):
    def test_find_triples_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triples = HandFinder.find_triples(hand)

        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0])[0], CardType.TRIPLE)
        self.assertEqual(HandClassifier.classify(triples[0])[1], 14)

    def test_find_triples_with_extra(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 0)])
        triples = HandFinder.find_triples(hand)

        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0])[1], 14)


class TestFindFives(ImportGuard):
    def test_find_straight(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(9, 1)])
        fives = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(p)[0] for p in fives if HandClassifier.classify(p) is not None]
        self.assertIn(CardType.STRAIGHT, types)

    def test_find_flush(self):
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(14, 2)])
        fives = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(p)[0] for p in fives if HandClassifier.classify(p) is not None]
        self.assertIn(CardType.FLUSH, types)

    def test_find_full_house(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 0), Card(5, 2)])
        fives = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(p)[0] for p in fives if HandClassifier.classify(p) is not None]
        self.assertIn(CardType.FULL_HOUSE, types)

    def test_find_four_of_a_kind(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1), Card(9, 2)])
        fives = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(p)[0] for p in fives if HandClassifier.classify(p) is not None]
        self.assertIn(CardType.FOUR_OF_A_KIND, types)

    def test_find_straight_flush(self):
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(14, 2)])
        fives = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(p)[0] for p in fives if HandClassifier.classify(p) is not None]
        self.assertIn(CardType.STRAIGHT_FLUSH, types)


class TestGetAllValidPlays(ImportGuard):
    def test_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        plays = HandFinder.get_all_valid_plays(hand, None)

        # 首回合僅允許單張 3♣。
        self.assertEqual(plays, [[Card(3, 0)]])

    def test_with_last_single(self):
        hand = Hand([Card(3, 0), Card(6, 1), Card(10, 3), Card(14, 2)])
        last_play = [Card(5, 0)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)

        self.assertTrue(all(len(p) == 1 for p in plays))
        self.assertTrue(all(HandClassifier.classify(p)[0] == CardType.SINGLE for p in plays))
        self.assertTrue(all(HandClassifier.compare(p, last_play) > 0 for p in plays))

    def test_with_last_pair(self):
        hand = Hand([Card(6, 0), Card(6, 3), Card(8, 1), Card(8, 2), Card(14, 3)])
        last_play = [Card(5, 1), Card(5, 2)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)

        self.assertTrue(all(len(p) == 2 for p in plays))
        self.assertTrue(all(HandClassifier.classify(p)[0] == CardType.PAIR for p in plays))
        self.assertTrue(all(HandClassifier.compare(p, last_play) > 0 for p in plays))

    def test_no_valid(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        last_play = [Card(15, 3)]  # 2♠ 幾乎是單張最大
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(plays, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
