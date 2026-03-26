"""Phase 1 資料模型：Card、Deck、Hand、Player。"""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable


@dataclass(frozen=True)
class Card:
    """單張撲克牌。

    rank: 3-15（14 代表 A，15 代表 2）
    suit: 0-3（0=♣, 1=♦, 2=♥, 3=♠）
    """

    rank: int
    suit: int

    _SUIT_SYMBOLS = {0: "♣", 1: "♦", 2: "♥", 3: "♠"}
    _RANK_SYMBOLS = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
    }

    def __repr__(self) -> str:
        rank_text = self._RANK_SYMBOLS.get(self.rank, str(self.rank))
        suit_text = self._SUIT_SYMBOLS[self.suit]
        return f"{suit_text}{rank_text}"

    def to_sort_key(self) -> tuple[int, int]:
        """回傳可用於排序與比較的鍵值。"""
        return (self.rank, self.suit)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.to_sort_key() < other.to_sort_key()


class Deck:
    """52 張牌組，提供洗牌與發牌功能。"""

    def __init__(self) -> None:
        self.cards = self._create_cards()

    @staticmethod
    def _create_cards() -> list[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        if n <= 0:
            return []
        take = min(n, len(self.cards))
        dealt = self.cards[:take]
        self.cards = self.cards[take:]
        return dealt


class Hand(list[Card]):
    """玩家手牌容器。"""

    def __init__(self, cards: Iterable[Card] | None = None) -> None:
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        # 測試預期：rank 倒序，且同 rank 時 suit 也倒序（♠ 到 ♣）。
        self.sort(key=lambda card: (-card.rank, -card.suit))

    def find_3_clubs(self) -> Card | None:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards: Iterable[Card]) -> None:  # type: ignore[override]
        # 移除多張牌；不存在的牌忽略，避免中斷流程。
        for card in cards:
            try:
                super().remove(card)
            except ValueError:
                continue


class Player:
    """玩家資料模型。"""

    def __init__(self, name: str, is_ai: bool = False) -> None:
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: Iterable[Card]) -> list[Card]:
        cards_list = list(cards)
        self.hand.remove(cards_list)
        return cards_list
