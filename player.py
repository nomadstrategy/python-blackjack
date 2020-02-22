import logging

logging.basicConfig(level=logging.DEBUG)
# could make a project logger


class Player:
    def __init__(self, buyin=100, min_stake=1, max_stake=None, name="Player"):
        self.buyin = buyin
        self.chips = buyin
        self.min_stake = min_stake
        self.max_stake = max_stake
        self.name = name
        self.hand = []
        self.wager = 0

    @staticmethod
    def register_player():
        playername = input("Name? : ")
        buyin = int(input("Enter buyin amount: $"))
        max_stake = int(input("Enter your max stake per bet: $"))
        min_stake = max_stake / 100
        return Player(buyin, min_stake=min_stake, max_stake=max_stake, name=playername)

    def topup(self, amount):
        logging.debug(f"old chipstack: ${self.chips}; adding ${amount}")
        self.chips += amount
        logging.debug(f"new chipstack: ${self.chips}")

    def check_bet_legality(self):
        def legal_bet(self, amount):
            if amount > self.chips:
                print(
                    f"Illegal bet of ${amount}. \
                        Please reduce your bet or add more chips. ${amount} > ${self.chips}"
                )

            elif amount < self.min_stake:
                print(f"${amount} lower than minimum acceptable wager")
            elif self.max_stake and amount > self.max_stake:
                print(f"${amount} higher than your max stake of ${self.max_stake}")
            else:
                return True

        return legal_bet

    # @check_bet_legality
    def bet(self, amount):
        # TODO: decorator: amount <= self.max_bet
        self.wager = amount
        print(f"amount: {amount} -- wager : ${self.wager}")
        logging.warning(f"${amount} wager: chipstack before: ${self.chips}")
        logging.warning(f"${self.wager} being deducted")
        self.chips -= amount
        logging.warning(f"${self.chips}")
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


p1 = Player(500, max_stake=100)

p1.bet(100)
print(p1.wager)
