from itertools import combinations
from typing import List, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier

class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        return [[c] for c in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        res = []
        ranks = {}
        for c in hand: ranks.setdefault(c.rank, []).append(c)
        for r, cards in ranks.items():
            if len(cards) >= 2: res.extend(list(combinations(cards, 2)))
        return [list(c) for c in res]

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        res = []
        ranks = {}
        for c in hand: ranks.setdefault(c.rank, []).append(c)
        for r, cards in ranks.items():
            if len(cards) >= 3: res.extend(list(combinations(cards, 3)))
        return [list(c) for c in res]

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        return [] # Simplified for now

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        return None

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        all_plays = HandFinder.find_singles(hand) + HandFinder.find_pairs(hand) + HandFinder.find_triples(hand)
        valid = []
        for play in all_plays:
            if not last_play or HandClassifier.can_play(last_play, play):
                if last_play and len(play) != len(last_play): continue
                valid.append(play)
        return valid
