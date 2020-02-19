import logging
from cards import Cards, Deck
from player import Player

logging.basicConfig(level=logging.DEBUG)


class Blackjack:
    # def __init__(self, *args, **kwargs):
    def __init__(self, *Players, shoes=6, min_wager=None, max_wager=None):
        self.players = Players
        logging.debug(self.players)
        self.bets = None
        self.shoes = shoes
        self.min_wager = min_wager
        self.max_wager = max_wager
        # bets = {'player_one': 100, 'p2': 55}

    def __str__(self):
        return f"""
        Welcome to Blackjack!\n
        Players are: {self.players}
        Table stakes: min wager: ${self.min_wager}
        Table stakes: max wager: ${self.max_wager}
        
        """


test_game = Blackjack(Player(525), shoes=6)
print(test_game)
