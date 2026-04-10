from typing import List, Optional, Tuple
from game.models import Card, Deck, Player
from game.classifier import HandClassifier
from game.ai import AIStrategy
from game.finder import HandFinder

class BigTwoGame:
    def __init__(self):
        self.deck = Deck()
        self.players: List[Player] = []
        self.current_player: int = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count: int = 0
        self.winner: Optional[Player] = None
        self.round_number: int = 0

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player("Player", is_ai=False)] + [Player(f"AI_{i}", is_ai=True) for i in range(1, 4)]
        for i in range(4):
            self.players[i].take_cards(self.deck.deal(13))
            self.players[i].hand.sort_desc()
            if any(c.rank == 3 and c.suit == 0 for c in self.players[i].hand):
                self.current_player = i
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1

    def play(self, player: Player, cards: List[Card]) -> bool:
        if not self._is_valid_play(cards): return False
        player.play_cards(cards)
        self.last_play = (cards, player.name)
        self.pass_count = 0
        self.check_winner()
        self.next_turn()
        return True

    def pass_(self, player: Player) -> bool:
        self.pass_count += 1
        self.next_turn()
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4
        self.check_round_reset()

    def _is_valid_play(self, cards: List[Card]) -> bool:
        if self.last_play is None: return True
        return HandClassifier.can_play(self.last_play[0], cards)

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1

    def check_winner(self) -> Optional[Player]:
        for p in self.players:
            if not p.hand:
                self.winner = p
                return p
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        if not player.is_ai: return False
        valid = HandFinder.get_all_valid_plays(player.hand, self.last_play[0] if self.last_play else None)
        best = AIStrategy.select_best(valid, player.hand, self.last_play is None)
        if best:
            self.play(player, best)
        else:
            self.pass_(player)
        return True
