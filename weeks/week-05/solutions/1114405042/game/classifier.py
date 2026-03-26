"""Phase 2 牌型分類與比較邏輯。"""

from __future__ import annotations

from collections import Counter
from enum import IntEnum
from typing import Optional

from .models import Card


class CardType(IntEnum):
    """牌型列舉，數值越大代表牌型越強。"""

    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """提供牌型分類、比較與合法出牌判斷。"""

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def _straight_high(ranks: list[int]) -> Optional[int]:
        """回傳順子最高點數；不是順子則回傳 None。

        支援一般順子與 A-2-3-4-5（以 5 當最高）。
        """
        uniq = sorted(set(ranks))
        if len(uniq) != 5:
            return None

        # 一般連號，例如 3,4,5,6,7
        if uniq[-1] - uniq[0] == 4 and all(uniq[i + 1] - uniq[i] == 1 for i in range(4)):
            return uniq[-1]

        # 特例：A-2-3-4-5 對應為 3,4,5,14,15
        if uniq == [3, 4, 5, 14, 15]:
            return 5

        return None

    @staticmethod
    def classify(cards: list[Card]) -> Optional[tuple[CardType, int, int]]:
        """分類牌型，回傳 (牌型, 關鍵點數, 花色資訊)。"""
        n = len(cards)
        if n == 0:
            return None

        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]
        rank_count = Counter(ranks)

        if n == 1:
            c = cards[0]
            return (CardType.SINGLE, c.rank, c.suit)

        if n == 2:
            if len(rank_count) == 1:
                rank = next(iter(rank_count))
                # 依測試規格，對子第三欄固定回傳 0。
                return (CardType.PAIR, rank, 0)
            return None

        if n == 3:
            if len(rank_count) == 1:
                rank = next(iter(rank_count))
                # 依測試規格，三條第三欄固定回傳 0。
                return (CardType.TRIPLE, rank, 0)
            return None

        if n != 5:
            return None

        is_flush = HandClassifier._is_flush(suits)
        straight_high = HandClassifier._straight_high(ranks)
        is_straight = straight_high is not None

        if is_flush and is_straight:
            return (CardType.STRAIGHT_FLUSH, straight_high, 0)

        if 4 in rank_count.values():
            four_rank = max(rank for rank, count in rank_count.items() if count == 4)
            return (CardType.FOUR_OF_A_KIND, four_rank, 0)

        if sorted(rank_count.values()) == [2, 3]:
            triple_rank = max(rank for rank, count in rank_count.items() if count == 3)
            return (CardType.FULL_HOUSE, triple_rank, 0)

        if is_flush:
            high_rank = max(ranks)
            return (CardType.FLUSH, high_rank, 0)

        if is_straight:
            return (CardType.STRAIGHT, straight_high, 0)

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        """比較兩手牌：1 代表 play1 較大，-1 代表 play2 較大，0 代表相同或無法比較。"""
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)

        if c1 is None and c2 is None:
            return 0
        if c1 is None:
            return -1
        if c2 is None:
            return 1

        t1, r1, s1 = c1
        t2, r2, s2 = c2

        if t1 != t2:
            return 1 if t1 > t2 else -1

        if r1 != r2:
            return 1 if r1 > r2 else -1

        # 單張可直接比花色；對子與三條以該組牌的最高花色當 tie-break。
        if t1 == CardType.SINGLE:
            if s1 != s2:
                return 1 if s1 > s2 else -1
            return 0

        if t1 in (CardType.PAIR, CardType.TRIPLE):
            max_suit_1 = max(card.suit for card in play1)
            max_suit_2 = max(card.suit for card in play2)
            if max_suit_1 != max_suit_2:
                return 1 if max_suit_1 > max_suit_2 else -1
            return 0

        if s1 != s2:
            return 1 if s1 > s2 else -1

        return 0

    @staticmethod
    def can_play(last_play: Optional[list[Card]], cards: list[Card]) -> bool:
        """判斷是否可出牌。"""
        current = HandClassifier.classify(cards)
        if current is None:
            return False

        # 首回合必須包含 3♣。
        if last_play is None:
            return any(card.rank == 3 and card.suit == 0 for card in cards)

        previous = HandClassifier.classify(last_play)
        if previous is None:
            return False

        # 一般情況需出同張數；避免用 2 張去壓 1 張等不合理情況。
        if len(cards) != len(last_play):
            return False

        return HandClassifier.compare(cards, last_play) > 0
