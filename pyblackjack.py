import logging
from cards import Cards, Deck
from player import Player

logging.basicConfig(level=logging.DEBUG)


class Blackjack:
    # def __init__(self, *args, **kwargs):
    def __init__(self, *Players, shoes=6, min_wager=None, max_wager=None):
        self.players = list(Players)
        # logging.debug(self.players)
        self.shoes = shoes
        self.deck = Deck(shuffle=True, amount=shoes)
        self.min_wager = min_wager
        self.max_wager = max_wager
        # bets = {'player_one': 100, 'p2': 55}
        self.bets = 0

    def take_bets(self):
        for player in self.players:
            wager = int(input("Enter your bet: $"))
            player.bet(wager)
            self.bets += player.wager

        # self.bets = {player.name: player.wager for player in Players}

    def deal_cards(self, *Players, amount=1):
        if not self.deck:
            print("Shuffling a new deck!")
            self.deck = Deck(shuffle=True)

        for player in Players:
            player.hand.extend(self.deck.deal(amount))

    def __str__(self):
        return f"""
        Welcome to Blackjack!\n
        Players are: {self.players}
        Table stakes: min wager: ${self.min_wager}
        Table stakes: max wager: ${self.max_wager}
        
        """


# # def setup_game():
# #     playername = input('Name? : ')
# #     buyin = int(input('Enter buyin amount: $'))
# #     max_stake = int(input('Enter your max stake per bet: $'))
# #     min_stake = max_stake/100
# #     return Player(buyin, max_stake=max_stake, name=playername)

# # register = setup_game()
# game_deck = Deck()
# player_one = Player(5000)
# player_two = Player(333, name="Joei")
# game = Blackjack(player_one, player_two, shoes=6)
# # print(game)

# game.deal_cards(player_one, player_two, amount=2)

# for player in game.players:
#     print(player.name)
#     print(player.hand)

# print(game.bets)

# game.take_bets()

