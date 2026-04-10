from typing import List, Optional

class Card:
    SUITS = ['♣', '♦', '♥', '♠']
    RANKS = {14: 'A', 15: '2', 11: 'J', 12: 'Q', 13: 'K', 10: 'T'}
    
    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit
        
    def __repr__(self) -> str:
        r = Card.RANKS.get(self.rank, str(self.rank))
        s = Card.SUITS[self.suit]
        return f"{s}{r}"
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
        
    def __lt__(self, other) -> bool:
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank
        
    def __hash__(self) -> int:
        return hash((self.rank, self.suit))
        
    def to_sort_key(self) -> tuple:
        return (self.rank, self.suit)

class Deck:
    def __init__(self):
        self.cards = self._create_cards()
        
    def _create_cards(self) -> List[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]
        
    def shuffle(self) -> None:
        import random
        random.shuffle(self.cards)
        
    def deal(self, n: int) -> List[Card]:
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt

class Hand(list):
    def __init__(self, cards: Optional[List[Card]] = None):
        super().__init__(cards or [])
        
    def sort_desc(self) -> None:
        self.sort(key=lambda c: (-c.rank, c.suit))
        
    def find_3_clubs(self) -> Optional[Card]:
        for c in self:
            if c.rank == 3 and c.suit == 0:
                return c
        return None
        
    def remove(self, cards: List[Card]) -> None:
        for c in cards:
            if c in self:
                super().remove(c)

class Player:
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
        
    def take_cards(self, cards: List[Card]) -> None:
        self.hand.extend(cards)
        
    def play_cards(self, cards: List[Card]) -> List[Card]:
        self.hand.remove(cards)
        return cards
