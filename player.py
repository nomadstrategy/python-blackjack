import logging

logging.basicConfig(level=logging.DEBUG)
# could make a project logger


class Player:
    def __init__(self, buyin, min_stake=1, max_stake=None, name="Player"):
        self.buyin = buyin
        self.chips = buyin
        self.min_stake = min_stake
        self.max_stake = max_stake
        self.name = name
        self.hand = []
        self.wager = 0

    def topup(self, amount):
        logging.debug(f"old chipstack: ${self.chips}; adding ${amount}")
        self.chips += amount
        logging.debug(f"new chipstack: ${self.chips}")

    def bet(self, amount):
        self.wager = amount
        logging.debug(f"${amount} wager: chipstack before: ${self.chips}")
        logging.debug(f"${self.wager} being deducted")
        self.chips -= amount
        logging.debug(f"${self.chips}")
        return self.wager

    # def receive_cards(self, Deck: object, amount=1):
    #     """taking in the game deck, add the amount of cards to the
    #     player's hand

    #     Arguments:
    #         Deck {class} -- [game deck object]

    #     Keyword Arguments:
    #         amount {int} -- [number of cards to receive] (default: {1})
    #     """
    #     self.hand.append(Deck.deal(amount))
    #     logging.debug(self.hand)

    def __str__(self):
        return f"Player '{self.name.capitalize()}' has ${self.chips} in chips."

