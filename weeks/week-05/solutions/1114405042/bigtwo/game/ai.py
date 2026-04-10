from typing import List, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier, CardType
from game.finder import HandFinder

class AIStrategy:
    TYPE_SCORES = {
        CardType.SINGLE: 1, CardType.PAIR: 2, CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4, CardType.FLUSH: 5, CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7, CardType.STRAIGHT_FLUSH: 8
    }
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        c = HandClassifier.classify(cards)
        if not c: return 0
        score = AIStrategy.TYPE_SCORES[c[0]] * 100 + c[1] * 10
        rem = len(hand) - len(cards)
        if rem == 0: score += AIStrategy.EMPTY_HAND_BONUS
        elif rem <= 3: score += AIStrategy.NEAR_EMPTY_BONUS
        score += sum(AIStrategy.SPADE_BONUS for card in cards if card.suit == 3)
        return score

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        if not valid_plays: return None
        if is_first:
            for play in valid_plays:
                for c in play:
                    if c.rank == 3 and c.suit == 0: return play
        best_play = None
        best_score = -1
        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play
        return best_play
