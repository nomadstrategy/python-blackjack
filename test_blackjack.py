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
from player import Player


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
    deck_copy = [card for card in deck_one.cards]
    assert deck_copy == deck_one.cards
    print(deck_copy)

    deck_one.shuffle()
    print(deck_one.cards)
    assert deck_copy != deck_one.cards


def test_dealing_cards(amount=1):
    # generator for decks?
    deck = Deck(shuffle=True)
    test_hand_one = deck.deal(cards=2)
    test_hand_two = deck.deal(cards=2)
    assert len(test_hand_one) == 2
    assert test_hand_one != test_hand_two
    test_hand_three = deck.deal(cards=1384)
    assert len(test_hand_three) == 1384
    print(test_hand_three)
    # hand deck exhaustion smoothly
    test_hand_four = deck.deal(6)
    assert len(test_hand_four) == 6
    deck_two = Deck(shuffle=True)
    deck_three = Deck(shuffle=True)
    assert deck_two.cards != deck_three.cards

    print(test_hand_three)


def test_player_setup():
    p1 = Player(buyin=100, min_stake=10, max_stake=100)
    p2 = Player(500)
    assert p1.buyin == 100
    assert p1.chips == 100
    assert p1.min_stake == 10
    assert p2.chips == 500
    assert p2.max_stake == 500
    assert p1.max_stake == 100
    assert p2.min_stake == 1


def test_player_methods():
    deck = Deck(shuffle=True)
    p1 = Player(500)
    bet = p1.bet(200)
    assert p1.wager == 200
    assert p1.wager == 200
    assert p1.chips == 300
    # who does the pot 'belong to' -- blackjack class
    card = p1.receive_cards(deck)
    assert p1.hand
    cards = p1.receive_cards(deck, amount=50)
    assert len(p1.hand) == 50


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
# pom #3 75 min [x]
# pom #4 100 min []
