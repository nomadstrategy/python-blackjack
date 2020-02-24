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

    @staticmethod  # TODO: class method? blackjack namespace? module level?
    def register_player():
        playername = input("Name? : ")
        buyin = int(input("Enter buyin amount: $"))
        max_stake = int(input("Enter your max stake per bet: $"))
        min_stake = max_stake / 100
        return Player(buyin, min_stake=min_stake, max_stake=max_stake, name=playername)

    def topup(self, amount):
        # logging.debug(f"old chipstack: ${self.chips}; adding ${amount}")
        self.chips += amount
        # logging.debug(f"new chipstack: ${self.chips}")

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
    def bet(self, amount: int):
        # TODO: decorator: amount <= self.max_bet
        if amount > self.chips:
            raise Exception(
                f"Your bet of ${amount} is greater than your balance of ${self.min_stake}! Topup or reduce bet."
            )
        elif amount < self.min_stake:
            raise Exception(
                f"Your bet of ${amount} is under your minimum allowed bet of ${self.min_stake}"
            )
        elif self.max_stake and amount > self.max_stake:
            raise Exception(
                f"Your bet of ${amount} is over your maximum allowed bet of ${self.max_stake}"
            )
        else:
            self.wager = amount
            print(f"{self.name} is betting ${self.wager}")

            self.chips -= amount

            return self.wager

    def __str__(self):
        return f"Player '{self.name.capitalize()}' has ${self.chips} in chips."


# p = Player(500)

# p.bet(5000)
