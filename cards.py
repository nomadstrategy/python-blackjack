from dataclasses import dataclass


@dataclass
class Cards:
    """
    builds the cards for a standard 52 card deck of cards 
        a hand:
        ['Ac', 'Th', '2s', '9c']
        contains:
        'Ace of Clubs', 'Ten of Hearts', 'Deuce of Spades' and 'Nine of Clubs'
    """

    rank: str
    suit: str

    def __str__(self):
        return f"{self.rank}{self.suit}"


c = Cards("2", "c")
print(c)
# class Deck:
#     def __init__(self, shuffle=False):
