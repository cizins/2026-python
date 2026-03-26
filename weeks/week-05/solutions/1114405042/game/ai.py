"""Phase 4 AI 策略：以貪心分數選擇最佳出牌。"""

from __future__ import annotations

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class AIStrategy:
    """簡易 AI：根據牌型、點數與收尾能力做評分。"""

    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }

    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: list[Card], hand: Hand, is_first: bool = False) -> float:
        """計算單次出牌分數，分數越高越優先。"""
        classified = HandClassifier.classify(cards)
        if classified is None:
            return float("-inf")

        card_type, rank_value, _ = classified
        type_score = AIStrategy.TYPE_SCORES[card_type]

        score = type_score * 100 + rank_value * 10

        # 黑桃加分：鼓勵在同點數下偏好高花色。
        score += sum(AIStrategy.SPADE_BONUS for card in cards if card.suit == 3)

        remaining = len(hand) - len(cards)
        if remaining <= 1:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 2:
            score += AIStrategy.NEAR_EMPTY_BONUS

        # 首回合需要保守地遵守規則，不額外偏置即可。
        _ = is_first
        return float(score)

    @staticmethod
    def select_best(valid_plays: list[list[Card]], hand: Hand, is_first: bool = False) -> list[Card] | None:
        """從合法出牌中選擇分數最高者。"""
        if not valid_plays:
            return None

        if is_first:
            # 首回合優先單出 3♣；若不存在則退而求其次選包含 3♣ 的牌組。
            single_three_clubs = [play for play in valid_plays if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0]
            if single_three_clubs:
                return single_three_clubs[0]

            include_three_clubs = [play for play in valid_plays if any(card.rank == 3 and card.suit == 0 for card in play)]
            if include_three_clubs:
                return max(include_three_clubs, key=lambda play: AIStrategy.score_play(play, hand, is_first=True))

        return max(valid_plays, key=lambda play: AIStrategy.score_play(play, hand, is_first=is_first))
