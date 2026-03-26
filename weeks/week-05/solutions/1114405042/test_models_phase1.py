"""Phase 1 資料模型測試

對應測試目標：Card、Deck、Hand、Player
預期被測試模組：game/models.py

執行方式：
python -m unittest test_models_phase1.py -v
"""

import unittest
import importlib

# 先嘗試匯入待測試類別；若失敗，讓每個測試個別顯示清楚錯誤。
try:
    models = importlib.import_module("game.models")
    Card = models.Card
    Deck = models.Deck
    Hand = models.Hand
    Player = models.Player
    IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover
    Card = Deck = Hand = Player = None
    IMPORT_ERROR = exc


class ModelsImportGuard(unittest.TestCase):
    """共用基底：在每個測試前檢查匯入狀態。"""

    def setUp(self):
        if IMPORT_ERROR is not None:
            self.fail(f"無法匯入 game.models（{IMPORT_ERROR}）。請先完成 game/models.py 的實作。")


class TestCard(ModelsImportGuard):
    def test_card_creation(self):
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self):
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self):
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_card_compare_suit(self):
        self.assertTrue(Card(14, 3) > Card(14, 2))  # ♠ > ♥

    def test_card_compare_suit_2(self):
        self.assertTrue(Card(14, 2) > Card(14, 1))  # ♥ > ♦

    def test_card_compare_suit_3(self):
        self.assertTrue(Card(14, 1) > Card(14, 0))  # ♦ > ♣

    def test_card_compare_rank_2(self):
        self.assertTrue(Card(15, 0) > Card(14, 3))  # 2 > A

    def test_card_compare_rank_a(self):
        self.assertTrue(Card(14, 0) > Card(13, 3))  # A > K

    def test_card_compare_equal(self):
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self):
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(ModelsImportGuard):
    def test_deck_has_52_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks(self):
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        deck = Deck()
        original = list(deck.cards)

        # 為降低極低機率的「洗牌後順序剛好一樣」，最多嘗試 5 次。
        changed = False
        for _ in range(5):
            deck.shuffle()
            if deck.cards != original:
                changed = True
                break

        self.assertTrue(changed, "洗牌後牌序應改變")
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(set(deck.cards), set(original))

    def test_deal_5_cards(self):
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        deck = Deck()
        first = deck.deal(5)
        second = deck.deal(3)
        self.assertEqual(len(first), 5)
        self.assertEqual(len(second), 3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(ModelsImportGuard):
    def test_hand_creation(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(hand), 3)

    def test_hand_sort_desc(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        self.assertEqual(list(hand), [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)])

    def test_hand_find_3_clubs(self):
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self):
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self):
        c1 = Card(3, 0)
        c2 = Card(14, 3)
        c3 = Card(13, 2)
        hand = Hand([c1, c2, c3])
        hand.remove([c1, c3])
        self.assertEqual(list(hand), [c2])

    def test_hand_remove_not_found(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        before = list(hand)
        hand.remove([Card(7, 1)])
        self.assertEqual(list(hand), before)

    def test_hand_iteration(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(list(hand)), 2)


class TestPlayer(ModelsImportGuard):
    def test_player_human(self):
        player = Player("Player1", False)
        self.assertEqual(player.name, "Player1")
        self.assertFalse(player.is_ai)

    def test_player_ai(self):
        player = Player("AI_1", True)
        self.assertEqual(player.name, "AI_1")
        self.assertTrue(player.is_ai)

    def test_player_take(self):
        player = Player("P1")
        cards = [Card(3, 0), Card(14, 3)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)

    def test_player_play(self):
        player = Player("P1")
        c1 = Card(3, 0)
        c2 = Card(14, 3)
        player.take_cards([c1, c2])

        played = player.play_cards([c1])
        self.assertEqual(played, [c1])
        self.assertEqual(list(player.hand), [c2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
