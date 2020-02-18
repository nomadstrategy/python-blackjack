"""
simulate blackjack game with all featuers including insurance, 
graphics, etc. This is a much harder project than I have ever
tried before, so it is difficult work in progress.


User story:

Players can easily play a simulated blackjack game with a full
feature set, good enough to pass as a free lunch-tray video screen on the back
of the headrest of the plane seat infront of you.

Reqs
Cards are easy enough to work with and pass around to other objs
Decks generated smoothly, my_deck.shuffle() etc consistent calls
Smooth player chip buyin and exiting on tables
Nice printout of info
test driven development!
try logging instead of print debug
"""

from cards import Cards
from deck import Deck


def test_deck():

    """
    RED GREEN REFACTOR 
    a (failing) sanity test layout
    """
    deck = Deck()
    assert len(deck) == 52
    assert "As" in deck.cards
    # 'As' == 'Ace of Spades', default syntax for online games
    assert "6d" in deck.cards
    assert "Jh" in deck.cards
    assert "Tc" in deck.cards
    # '6 of diamonds', 'Jack of hearts', 'Ten of clubs'
    # assert "6 of Diamonds" in __dir__(cards)
    # #


# class Cards:
#     # dataclass
#     # suits, ranks

# class DeckGenerator:
#     # returns a deck of cards
#     # deck methods; deal, shuffle, iteration stuff, handle exhaustion

# class Blackjack:
#     # requests decks from generator, gather bets, deals cards
#     # scores hands, handles chips, shuffles cards
#     # registers players, cashouts etc

# class Player:
#     # datafields (name, buyin, set/get?,)
#     # Player.make_wager(500)
#     #

# #time logged: 25min
# # start pom #2 50min []
