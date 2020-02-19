import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)


@dataclass
class Cards:

    rank: str
    suit: str

    def __repr__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    """ 
        builds standard 52 card deck of cards 
        a hand:
        ['Ac', 'Th', '2s', '9c']
        contains:
        'Ace of Clubs', 'Ten of Hearts', 'Deuce of Spades' and 'Nine of Clubs'
    """

    RANKS = "2 3 4 5 6 7 8 9 T J Q K A".split()
    SUITS = "c d h s".split()

    def __init__(self, shuffle=False):
        self.cards = [Cards(rank, suit) for rank in self.RANKS for suit in self.SUITS]

        if shuffle:
            self.shuffle()

    def shuffle(self):
        import random

        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def deal(self, cards=1):
        while cards > len(self.cards):
            logging.debug(f"{cards} requested exceeds deck length of {len(self.cards)}")
            self.cards.extend(Deck().cards)
            logging.debug(f"Deck extended to {len(self.cards)} cards")
        return [self.cards.pop(0) for _ in range(cards)]

