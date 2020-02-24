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
import pytest
from cards import Cards, Deck
from player import Player
from pyblackjack import Blackjack


def test_Blackjack_sanity():
    p1 = Player(1000)
    p2 = Player(525)
    game = Blackjack(p1, p2)
    assert len(game.deck) == game.shoes * 52


def test_Blackjack_players():
    p1 = Player(buyin=1000, min_stake=1, max_stake=1000, name="Rainman")
    assert p1.name == "Joe"

    p2 = Player(300)
    assert p2.chips == 300

    game = Blackjack(p1, p2, shoes=6)
    game.deal_cards(p1, p2)

    # TODO: better syntax for calling hands, name ref or ?
    assert game.players[0].hand

    assert game.players[0].chips == 1000
    assert game.players[1].chips == 300

    p1.bet(p1.chips)  # all chips
    p2.bet(p2.chips)

    assert p1.chips == p2.chips

    # TODO: p1.wager(250) --> doesn't reg with
    # blackjack class, blackjack.wager should set?
    """
    # game.take_bets()
    # WARNING: inputting 250 here to pass..
    # TODO: REFACTOR TEST TO AVOID INPUT
    # assert p1.wager == 250
    # assert p2.wager == 250
    # assert game.bets == p1.wager + p2.wager
    """

    assert p1.chips == 0
    p1.topup(50000)
    assert p1.chips == 50000

    with pytest.raises(Exception):
        assert p2.topup("Q")


def test_Player_betting_restrictions():

    p = Player(100, min_stake=1, max_stake=50, name="Joe")

    assert p.min_stake == 1
    assert p.max_stake == 50
    with pytest.raises(Exception):
        assert p.bet(51)
    with pytest.raises(Exception):
        assert p.bet("Q5")
    with pytest.raises(Exception):
        assert p.bet(-1)
    p.bet(10)
    assert p.wager == 10

    p2 = Player(buyin=500)
    p2.bet(500)
    with pytest.raises(Exception):
        assert p.bet(500)  # TODO: Check that can't bet stack X2 over two hands

    assert p2.wager == 500


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
    # print(deck_copy)

    deck_one.shuffle()
    # print(deck_one.cards)
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
    test_hand_four = deck.deal(6)
    assert len(test_hand_four) == 6
    deck_two = Deck(shuffle=True)
    deck_three = Deck(shuffle=True)
    assert deck_two.cards != deck_three.cards


# SECTION NOTES:

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
#     # temporarily (?)#TODO: decide
#           remove Player.receive_cards(deck) -- convoluted
#     #         Players also do not have access to the Deck so dealer should
#     #         call that.
#
#           Players lists should be modified by dealers ; #TODO: setter/getter?

# #time logged: 25min   [x]
# # start pom #2 50min [x]
# pom #3 75 min [x]
# pom #4 100 min [x]
# pom #5 125 min [x]
# pom #6 150 min []
