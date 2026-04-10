from enum import IntEnum
from typing import List, Optional, Tuple
from game.models import Card

class CardType(IntEnum):
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class HandClassifier:
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        if not ranks or len(ranks) != 5: return False
        ranks = sorted(ranks)
        if ranks == [3, 4, 5, 14, 15]: return True # A-2-3-4-5
        for i in range(4):
            if ranks[i+1] - ranks[i] != 1: return False
        return True

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        if not suits or len(suits) != 5: return False
        return len(set(suits)) == 1

    @staticmethod
    def _count_ranks(cards: List[Card]) -> dict:
        counts = {}
        for c in cards:
            counts[c.rank] = counts.get(c.rank, 0) + 1
        return counts

    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        n = len(cards)
        if n == 0: return None
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        max_card = max(cards)
        counts = HandClassifier._count_ranks(cards)
        
        if n == 1:
            return (CardType.SINGLE, max_card.rank, max_card.suit)
        elif n == 2:
            if len(counts) == 1: return (CardType.PAIR, max_card.rank, max_card.suit)
        elif n == 3:
            if len(counts) == 1: return (CardType.TRIPLE, max_card.rank, max_card.suit)
        elif n == 5:
            is_st = HandClassifier._is_straight(ranks)
            is_fl = HandClassifier._is_flush(suits)
            if is_st and is_fl: return (CardType.STRAIGHT_FLUSH, max_card.rank, max_card.suit)
            if 4 in counts.values():
                val = [k for k, v in counts.items() if v == 4][0]
                return (CardType.FOUR_OF_A_KIND, val, 3) # Simplify suit
            if 3 in counts.values() and 2 in counts.values():
                val = [k for k, v in counts.items() if v == 3][0]
                return (CardType.FULL_HOUSE, val, 3)
            if is_fl: return (CardType.FLUSH, max_card.rank, max_card.suit)
            if is_st: return (CardType.STRAIGHT, max_card.rank, max_card.suit)
        return None

    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)
        if not c1 or not c2: return 0
        if c1[0] != c2[0]:
            if len(play1) == 5 and len(play2) == 5:
                return 1 if c1[0] > c2[0] else -1
            return 0 # Cannot compare different lengths unless valid 5-card combo
        if c1[1] != c2[1]: return 1 if c1[1] > c2[1] else -1
        if c1[2] != c2[2]: return 1 if c1[2] > c2[2] else -1
        return 0

    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        curr_class = HandClassifier.classify(cards)
        if not curr_class: return False
        if not last_play:
            # First round must contain 3 of clubs, assuming models handles this mostly
            for c in cards:
                if c.rank == 3 and c.suit == 0: return True
            return True # Not strictly enforced here unless specified
        return HandClassifier.compare(cards, last_play) > 0
