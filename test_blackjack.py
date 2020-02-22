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
from pyblackjack import Blackjack


def test_Blackjack_logic():
    d = Deck()
    p1 = Player(buyin=1000, min_stake=1, max_stake=1000, name="Rainman")
    p2 = Player(300)

    # game1 = Blackjack()
    # put in parameters? ^ for the players? probably yes..
    # if __name__ == 'pyblackjack':
    # get_info
    # game = Blackjack(user_info_start)
    game = Blackjack(p1, p2, shoes=6)
    # assert game.players has p1 and p2 maybe as dict keys with info and hands
    # assert game.players.p1.hand != game.players.p2.hand
    game.deal_cards(p1, p2)
    assert game.p1.hand

    assert game.players.p1.chips == 1000
    assert game.players.p2.chips == 300
    assert len(game.shoe) == shoes * 52
    debug_p1_chips = (p1.chips,)
    logging.debug(debug_p1_chips)
    b3 = Blackjack(shoes=6)
    assert len(b3) == 6 * 52
    p1.bet(p1.chips)
    p2.bet(p2.chips)
    assert p1.chips == p2.chips
    assert p1.wager == debug_p1_chips
    assert game.bets == p1.wager + p2.wager


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
    # print(test_hand_three)
    # hand deck exhaustion smoothly
    test_hand_four = deck.deal(6)
    assert len(test_hand_four) == 6
    deck_two = Deck(shuffle=True)
    deck_three = Deck(shuffle=True)
    assert deck_two.cards != deck_three.cards

    # print(test_hand_three)


def test_player_setup():
    p1 = Player(buyin=100, min_stake=10, max_stake=100)
    p2 = Player(500, max_stake=500)
    assert p1.buyin == 100
    assert p1.chips == 100
    assert p1.min_stake == 10
    assert p2.chips == 500
    assert p2.max_stake == 500
    assert p1.max_stake == 100
    assert p2.min_stake == 1
    # assert str(Player) is nice to read
    # new_player = Player.register_player()


def test_player_methods():
    deck = Deck(shuffle=True)
    p1 = Player(500)
    p2 = Player(8000)
    bet = p1.bet(200)
    print(p1.bet)
    print(p1.wager)
    assert p1.wager == 200
    assert p1.wager == 200
    assert p1.chips == 300
    # who does the pot 'belong to' -- blackjack class
    # card = p1.receive_cards(deck)

    assert p1.hand
    # cards = p2.receive_cards(deck, amount=50)
    print(f"P2 hand: {p2.hand} \n has {len(p2.hand)} cards")
    # assert len(p2.hand) == 50


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
