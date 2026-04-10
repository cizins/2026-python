import unittest
from game.models import Card, Deck, Hand, Player

class TestModels(unittest.TestCase):
    def test_card_creation(self):
        c = Card(rank=14, suit=3)
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)
        
    def test_card_repr_ace(self):
        self.assertEqual(repr(Card(14, 3)), "♠A")
        
    def test_card_repr_three(self):
        self.assertEqual(repr(Card(3, 0)), "♣3")
        
    def test_card_compare_suit(self):
        self.assertTrue(Card(14, 3) > Card(14, 2))
        
    def test_card_compare_suit_2(self):
        self.assertTrue(Card(14, 2) > Card(14, 1))
        
    def test_card_compare_suit_3(self):
        self.assertTrue(Card(14, 1) > Card(14, 0))
        
    def test_card_compare_rank_2(self):
        self.assertTrue(Card(15, 0) > Card(14, 3))
        
    def test_card_compare_rank_a(self):
        self.assertTrue(Card(14, 0) > Card(13, 3))
        
    def test_card_compare_equal(self):
        self.assertFalse(Card(14, 3) > Card(14, 3))
        
    def test_card_sort_key(self):
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))
        
    def test_deck_has_52_cards(self):
        self.assertEqual(len(Deck().cards), 52)
        
    def test_deck_all_unique(self):
        self.assertEqual(len(set(Deck().cards)), 52)
        
    def test_deck_all_ranks(self):
        ranks = {c.rank for c in Deck().cards}
        self.assertEqual(ranks, set(range(3, 16)))
        
    def test_deck_all_suits(self):
        suits = {c.suit for c in Deck().cards}
        self.assertEqual(suits, {0, 1, 2, 3})
        
    def test_deck_shuffle(self):
        d1 = Deck()
        d2 = Deck()
        d2.shuffle()
        self.assertNotEqual(d1.cards, d2.cards)
        
    def test_deal_5_cards(self):
        d = Deck()
        c = d.deal(5)
        self.assertEqual(len(c), 5)
        self.assertEqual(len(d.cards), 47)
        
    def test_deal_multiple(self):
        d = Deck()
        d.deal(5)
        d.deal(3)
        self.assertEqual(len(d.cards), 44)
        
    def test_deal_exceed(self):
        d = Deck()
        c = d.deal(60)
        self.assertEqual(len(c), 52)
        self.assertEqual(len(d.cards), 0)
        
    def test_hand_creation(self):
        h = Hand([Card(14,3), Card(3,0), Card(4,1)])
        self.assertEqual(len(h), 3)
        
    def test_hand_sort_desc(self):
        h = Hand([Card(3,0), Card(14,3), Card(3,3), Card(13,2)])
        h.sort_desc()
        self.assertEqual(h, [Card(14,3), Card(13,2), Card(3,0), Card(3,3)])
        
    def test_hand_find_3_clubs(self):
        h = Hand([Card(14,3), Card(3,0), Card(3,1)])
        self.assertEqual(h.find_3_clubs(), Card(3,0))
        
    def test_hand_find_3_clubs_none(self):
        h = Hand([Card(14,3), Card(3,1)])
        self.assertIsNone(h.find_3_clubs())
        
    def test_hand_remove(self):
        h = Hand([Card(14,3), Card(3,0)])
        h.remove([Card(14,3)])
        self.assertEqual(len(h), 1)
        self.assertEqual(h[0], Card(3,0))
        
    def test_hand_remove_not_found(self):
        h = Hand([Card(14,3)])
        h.remove([Card(3,0)])
        self.assertEqual(len(h), 1)
        
    def test_hand_iteration(self):
        h = Hand([Card(14,3), Card(3,0)])
        self.assertEqual(len(list(h)), 2)
        
    def test_player_human(self):
        p = Player("Player1", False)
        self.assertFalse(p.is_ai)
        
    def test_player_ai(self):
        p = Player("AI_1", True)
        self.assertTrue(p.is_ai)
        
    def test_player_take(self):
        p = Player("P1")
        p.take_cards([Card(14,3), Card(3,0)])
        self.assertEqual(len(p.hand), 2)
        
    def test_player_play(self):
        p = Player("P1")
        p.take_cards([Card(14,3), Card(3,0)])
        played = p.play_cards([Card(14,3)])
        self.assertEqual(len(p.hand), 1)
        self.assertEqual(played, [Card(14,3)])

if __name__ == '__main__':
    unittest.main()
