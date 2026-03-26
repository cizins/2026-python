"""Phase 4 AI 策略測試

對應測試目標：AIStrategy
預期被測試模組：game/ai.py

執行方式：
python -m unittest test_ai_phase4.py -v
"""

import importlib
import unittest

# 動態匯入：可在尚未完成實作時給出明確失敗原因。
try:
    models = importlib.import_module("game.models")
    classifier_mod = importlib.import_module("game.classifier")
    finder_mod = importlib.import_module("game.finder")
    ai_mod = importlib.import_module("game.ai")

    Card = models.Card
    Hand = models.Hand
    CardType = classifier_mod.CardType
    HandClassifier = classifier_mod.HandClassifier
    HandFinder = finder_mod.HandFinder
    AIStrategy = ai_mod.AIStrategy
    IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    Card = Hand = CardType = HandClassifier = HandFinder = AIStrategy = None
    IMPORT_ERROR = exc


class ImportGuard(unittest.TestCase):
    """共用前置檢查。"""

    def setUp(self):
        if IMPORT_ERROR is not None:
            self.fail(f"無法匯入 game.ai 或其相依模組：{IMPORT_ERROR}")


class TestScorePlay(ImportGuard):
    """評分函數測試。"""

    def test_score_single(self):
        # 單張 A（非黑桃）且手牌不在 near-empty 狀態，預期 1*100 + 14*10 = 240。
        hand = Hand([Card(14, 2), Card(3, 0), Card(5, 1), Card(7, 3)])
        score = AIStrategy.score_play([Card(14, 2)], hand, is_first=False)
        self.assertEqual(score, 240)

    def test_score_pair_higher(self):
        hand = Hand([Card(10, 0), Card(10, 1), Card(10, 2), Card(6, 3)])
        score_single = AIStrategy.score_play([Card(10, 2)], hand)
        score_pair = AIStrategy.score_play([Card(10, 0), Card(10, 1)], hand)
        self.assertGreater(score_pair, score_single)

    def test_score_triple_higher(self):
        hand = Hand([Card(9, 0), Card(9, 1), Card(9, 2), Card(3, 3)])
        score_pair = AIStrategy.score_play([Card(9, 0), Card(9, 1)], hand)
        score_triple = AIStrategy.score_play([Card(9, 0), Card(9, 1), Card(9, 2)], hand)
        self.assertGreater(score_triple, score_pair)

    def test_score_near_empty(self):
        # 出 1 張後手牌剩 1 張，應觸發「清手加分」，總分需明顯大於 10000。
        hand = Hand([Card(14, 2), Card(3, 0)])
        score = AIStrategy.score_play([Card(14, 2)], hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        # 出 1 張後手牌剩 2 張，應有 near-empty 額外加分。
        hand = Hand([Card(8, 1), Card(6, 2), Card(4, 3)])
        score = AIStrategy.score_play([Card(8, 1)], hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        # 同點數單張下，♠ 應比非♠高（黑桃加分）。
        hand = Hand([Card(14, 3), Card(14, 2), Card(9, 0), Card(7, 1)])
        score_spade = AIStrategy.score_play([Card(14, 3)], hand)
        score_heart = AIStrategy.score_play([Card(14, 2)], hand)
        self.assertGreater(score_spade, score_heart)


class TestSelectBest(ImportGuard):
    """最佳出牌選擇測試。"""

    def test_select_best(self):
        hand = Hand([Card(10, 0), Card(10, 1), Card(6, 3)])
        valid_plays = [[Card(6, 3)], [Card(10, 0), Card(10, 1)]]
        best = AIStrategy.select_best(valid_plays, hand, is_first=False)
        self.assertEqual(best, [Card(10, 0), Card(10, 1)])

    def test_select_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        valid_plays = [[Card(14, 3)], [Card(3, 0)], [Card(13, 2)]]
        best = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(best, [Card(3, 0)])

    def test_select_empty(self):
        hand = Hand([Card(3, 0), Card(5, 1)])
        self.assertIsNone(AIStrategy.select_best([], hand, is_first=False))


class TestAIStrategyBehavior(ImportGuard):
    """完整策略行為測試。"""

    def test_ai_always_plays(self):
        hand = Hand([Card(6, 3), Card(8, 1), Card(10, 2)])
        last_play = [Card(5, 0)]
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)

        # 有合法出牌時，AI 應選出其中一手而不是 None。
        self.assertTrue(len(valid_plays) > 0)
        best = AIStrategy.select_best(valid_plays, hand, is_first=False)
        self.assertIsNotNone(best)
        self.assertIn(best, valid_plays)

    def test_ai_prefers_high(self):
        hand = Hand([Card(6, 0), Card(10, 2), Card(14, 3)])
        last_play = [Card(5, 1)]
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        best = AIStrategy.select_best(valid_plays, hand, is_first=False)

        # 在可接單張時，應偏好較高分（通常是點數更高）的牌。
        self.assertEqual(best, [Card(14, 3)])

    def test_ai_try_empty(self):
        hand = Hand([Card(14, 3)])
        valid_plays = [[Card(14, 3)]]
        best = AIStrategy.select_best(valid_plays, hand, is_first=False)

        # 僅剩最後一張時，應直接出完。
        self.assertEqual(best, [Card(14, 3)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
