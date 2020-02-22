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
        self.deck = Deck(shuffle=True)
        self.min_wager = min_wager
        self.max_wager = max_wager
        # bets = {'player_one': 100, 'p2': 55}

    def deal_cards(self, *Players, amount=1):
        if not self.deck:
            print("Shuffling a new deck!")
            self.deck = Deck(shuffle=True)

        for player in Players:
            player.hand.append(self.deck.deal(amount))

    def __str__(self):
        return f"""
        Welcome to Blackjack!\n
        Players are: {self.players}
        Table stakes: min wager: ${self.min_wager}
        Table stakes: max wager: ${self.max_wager}
        
        """


# def setup_game():
#     playername = input('Name? : ')
#     buyin = int(input('Enter buyin amount: $'))
#     max_stake = int(input('Enter your max stake per bet: $'))
#     min_stake = max_stake/100
#     return Player(buyin, max_stake=max_stake, name=playername)

# register = setup_game()
game_deck = Deck()
player_one = Player(5000)
player_two = Player(333, name="Joei")
test_game = Blackjack(player_one, player_two, shoes=6)
print(test_game)

test_game.deal_cards(player_one)
print(player_one.hand)

