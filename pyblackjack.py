import logging
from cards import Cards, Deck
from player import Player

logging.basicConfig(level=logging.DEBUG)


class Blackjack:
    # TODO: del Player if bust?
    def __init__(self, shoes=6, min_wager=1, max_wager=1_000_000, **Players):
        self.players = Players
        self.shoes = shoes
        self.deck = Deck(shuffle=True, amount=shoes)
        self.min_wager = min_wager
        self.max_wager = max_wager
        # bets = {'player_one': 100, 'p2': 55}
        self.bets = 0

    def take_bets(self):
        for player in self.players:
            logging.debug(type(self.players[player]))
            wager = int(input("Enter your bet: $"))
            logging.debug(type(self.players["Player #1"]))
            self.players[player].bet(wager)
            self.bets += self.players[player].wager

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


def main():
    """ sloppy implementation of game logic """
    print("Welcome to Blackjack!")

    dealer = Player(buyin=1_000_000_000, name="Dealer")
    players = {}
    print("Registering players! Take your seats.")
    # player_one = Player.register_player()
    # # TODO: refactor this!
    # prompt = input("Seat another player? [Y]es, [N]o")
    # if prompt.upper() != "Y":
    #     pass
    # else:
    #     player_two = Player.register_player()

    # for i, player in enumerate(range(6)):
    #     prompt = input("Seat a player? [Y]es, [N]o")
    #     if prompt.upper() != "Y":
    #         break
    #     else:
    #         players["player #" + str(i + 1)] = Player.register_player()

    players["Player #1"] = Player(100, max_stake=50, name="Rainman")

    # TODO: remove this palceholder ^

    blackjack = Blackjack(shoes=6, **players)

    blackjack.take_bets()


if __name__ == "__main__":
    main()
