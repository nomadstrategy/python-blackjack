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

from cards import Cards, Deck


def test_deck_setup():
    """
    RED GREEN REFACTOR 
    a (failing) sanity test layout
    """
    deck = Deck()
    assert len(deck) == 52
    assert Cards("A", "s") in deck.cards
    assert Cards("6", "d") in deck.cards
    assert Cards("J", "h") in deck.cards
    assert Cards("T", "c") in deck.cards


def test_shuffle_deck():
    deck_one = Deck(shuffle=True)
    deck_two = Deck(shuffle=True)
    deck_three = Deck(shuffle=False)
    deck_four = Deck(shuffle=False)
    assert deck_one.cards != deck_two.cards
    assert deck_three.cards == deck_four.cards
    deck_copy = deck_one.cards
    assert deck_copy == deck_one.cards
    deck_one.shuffle()
    assert deck_copy != deck_one.cards


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
# # start pom #2 50min [x]
