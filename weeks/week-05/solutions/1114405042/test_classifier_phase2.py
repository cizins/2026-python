"""Phase 2 牌型分類測試

對應測試目標：CardType、HandClassifier
預期被測試模組：game/classifier.py

執行方式：
python -m unittest test_classifier_phase2.py -v
"""

import importlib
import unittest

# 動態匯入：避免在尚未完成實作前出現硬性匯入失敗。
try:
    models = importlib.import_module("game.models")
    classifier_mod = importlib.import_module("game.classifier")

    Card = models.Card
    CardType = classifier_mod.CardType
    HandClassifier = classifier_mod.HandClassifier
    IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    Card = CardType = HandClassifier = None
    IMPORT_ERROR = exc


class ImportGuard(unittest.TestCase):
    """共用檢查：若目標模組尚未完成，測試會給出清楚訊息。"""

    def setUp(self):
        if IMPORT_ERROR is not None:
            self.fail(f"無法匯入 game.classifier 或 game.models：{IMPORT_ERROR}")


class TestCardTypeEnum(ImportGuard):
    """CardType 列舉值測試。"""

    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


class TestClassifySingle(ImportGuard):
    """單張分類測試。"""

    def test_classify_single_ace(self):
        result = HandClassifier.classify([Card(14, 3)])
        self.assertEqual(result, (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        result = HandClassifier.classify([Card(15, 0)])
        self.assertEqual(result, (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        result = HandClassifier.classify([Card(3, 0)])
        self.assertEqual(result, (CardType.SINGLE, 3, 0))


class TestClassifyPair(ImportGuard):
    """對子分類測試。"""

    def test_classify_pair(self):
        result = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result, (CardType.PAIR, 14, 0))

    def test_classify_pair_diff_rank(self):
        result = HandClassifier.classify([Card(14, 3), Card(13, 3)])
        self.assertIsNone(result)

    def test_classify_pair_from_three(self):
        # 原始需求寫「從三條取兩張」，本質仍是兩張同點數對子。
        result = HandClassifier.classify([Card(14, 3), Card(14, 1)])
        self.assertEqual(result, (CardType.PAIR, 14, 0))


class TestClassifyTriple(ImportGuard):
    """三條分類測試。"""

    def test_classify_triple(self):
        result = HandClassifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)])
        self.assertEqual(result, (CardType.TRIPLE, 14, 0))

    def test_classify_triple_not_enough(self):
        # 兩張且點數不同，不可能形成三條。
        result = HandClassifier.classify([Card(14, 3), Card(13, 2)])
        self.assertIsNone(result)


class TestClassifyFiveCards(ImportGuard):
    """五張牌型分類測試。"""

    def test_classify_straight(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self):
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self):
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0))

    def test_classify_straight_flush(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


class TestCompare(ImportGuard):
    """牌型比較測試。"""

    def test_compare_single_rank(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(13, 3)]), 1)

    def test_compare_single_suit(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(14, 2)]), 1)

    def test_compare_pair_rank(self):
        p1 = [Card(14, 3), Card(14, 2)]
        p2 = [Card(13, 3), Card(13, 2)]
        self.assertEqual(HandClassifier.compare(p1, p2), 1)

    def test_compare_pair_suit(self):
        p1 = [Card(14, 3), Card(14, 2)]
        p2 = [Card(14, 1), Card(14, 0)]
        self.assertEqual(HandClassifier.compare(p1, p2), 1)

    def test_compare_different_type(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3), Card(14, 2)], [Card(15, 0)]), 1)

    def test_compare_flush_vs_straight(self):
        flush = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        straight = [Card(3, 1), Card(4, 2), Card(5, 3), Card(6, 0), Card(7, 1)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(ImportGuard):
    """合法出牌規則測試。"""

    def test_can_play_first_3clubs(self):
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))

    def test_can_play_same_type(self):
        last_play = [Card(5, 1), Card(5, 2)]
        cards = [Card(6, 0), Card(6, 3)]
        self.assertTrue(HandClassifier.can_play(last_play, cards))

    def test_can_play_diff_type(self):
        last_play = [Card(5, 1), Card(5, 2)]
        cards = [Card(6, 3)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))

    def test_can_play_not_stronger(self):
        last_play = [Card(10, 1), Card(10, 2)]
        cards = [Card(5, 0), Card(5, 3)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))


if __name__ == "__main__":
    unittest.main(verbosity=2)
