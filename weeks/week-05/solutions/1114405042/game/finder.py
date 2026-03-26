"""Phase 3 牌型搜尋邏輯。"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from .classifier import HandClassifier
from .models import Card, Hand


class HandFinder:
    """依據手牌找出所有可用牌型組合。"""

    @staticmethod
    def _group_by_rank(hand: Hand) -> dict[int, list[Card]]:
        groups: dict[int, list[Card]] = defaultdict(list)
        for card in hand:
            groups[card.rank].append(card)
        return groups

    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        groups = HandFinder._group_by_rank(hand)
        plays: list[list[Card]] = []
        for rank in sorted(groups):
            same_rank_cards = groups[rank]
            if len(same_rank_cards) < 2:
                continue
            for comb in combinations(same_rank_cards, 2):
                plays.append(list(comb))
        return plays

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        groups = HandFinder._group_by_rank(hand)
        plays: list[list[Card]] = []
        for rank in sorted(groups):
            same_rank_cards = groups[rank]
            if len(same_rank_cards) < 3:
                continue
            for comb in combinations(same_rank_cards, 3):
                plays.append(list(comb))
        return plays

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        plays: list[list[Card]] = []
        seen: set[tuple[tuple[int, int], ...]] = set()

        for comb in combinations(hand, 5):
            candidate = list(comb)
            classified = HandClassifier.classify(candidate)
            if classified is None:
                continue

            # 只收五張大牌型（避免把非五張牌型混入）。
            if classified[0] not in {
                classified[0].STRAIGHT,
                classified[0].FLUSH,
                classified[0].FULL_HOUSE,
                classified[0].FOUR_OF_A_KIND,
                classified[0].STRAIGHT_FLUSH,
            }:
                continue

            signature = tuple(sorted((card.rank, card.suit) for card in candidate))
            if signature in seen:
                continue
            seen.add(signature)
            plays.append(candidate)

        return plays

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: list[Card] | None) -> list[list[Card]]:
        # 首回合限定出 3♣。
        if last_play is None:
            three_clubs = next((card for card in hand if card.rank == 3 and card.suit == 0), None)
            return [[three_clubs]] if three_clubs is not None else []

        length = len(last_play)
        if length == 1:
            candidates = HandFinder.find_singles(hand)
        elif length == 2:
            candidates = HandFinder.find_pairs(hand)
        elif length == 3:
            candidates = HandFinder.find_triples(hand)
        elif length == 5:
            candidates = HandFinder.find_fives(hand)
        else:
            return []

        return [play for play in candidates if HandClassifier.can_play(last_play, play)]
