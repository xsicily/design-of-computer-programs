# -----------
# User Instructions
# 
# Modify the poker() function to return the best hand from a list of hands
# according to the hand_rank() function. Since we have
# not yet written hand_rank(), clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 
#
# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable,
# according to the function specified by key.


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    return allmax(hands, key=hand_rank)


def allmax(hands, key=None):
    """Return a list of all items equal to the max of the iterable."""
    # Your code here.
    winner = []
    max_hand = max(hands, key = hand_rank)
    for hand in hands:
        if hand_rank(hand) == hand_rank(max_hand):
            winner.append(hand)
    return winner

# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10,
# 'J' to 11, etc...


def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks


# should output [14, 13, 4, 3]


print(card_ranks(['AC', '3D', '4S', 'KH']))


# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.


def straight(ranks):
    """Return True if the !ordered ranks form a 5-card straight."""
    # Your code here.
    if len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4:
        return True
    else:
        return False


def flush(hand):
    """Return True if all the cards have the same suit."""
    # Your code here.
    suit = [s for r, s in hand]
    if len(set(suit)) == 1:
        return True
    else:
        return False

# Define a function, kind(n, ranks).


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

# Define a function, two_pair(ranks).


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    if len(set(ranks)) == 3:
        return ranks[0], ranks[2]
    else:
        return None


"""
def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return (pair, low_pair)
    else:
        return None
"""

# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands.
#
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).
#


def group(items):
    """Return a list of [(count, x)...], highest count first, then highest x first"""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

def unzip(pairs): return zip(*pairs)


def hand_rank(hand):
    """Return a value indicating how high the hand ranks"""
    # DRY: don't repeat yourself!
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


"""
optimized solution:
def hand_rank(hand):
    # Return a value indicating how high the hand ranks
    # counts is the count of each rank; ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight= len(ranks) == 5 and max(ranks) - min(ranks) == 4           # straight flush
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else
            8 if straight and flush else
            7 if (4, 1) == counts else
            6 if (3, 2) == counts else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) == counts else
            2 if (2, 2, 1) == counts else
            1 if (2, 1, 1, 1) == counts else
            0), ranks
"""


"""
optimized solution
count_rankings = {(5,):10, (4, 1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2,
                (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}
def hand_rank(hand):
    # Return a value indicating how high the hand ranks
    # counts is the count of each rank; ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight= len(ranks) == 5 and max(ranks) - min(ranks) == 4           # straight flush
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks
"""
# Modify the test() function to include two new test cases:
# 1) four of a kind (fk) vs. full house (fh) returns fk.
# 2) full house (fh) vs. full house (fh) returns fh.
# Modify the test() function to include two new test cases:
# 1) A single hand.
# 2) 100 hands.
# Modify the test() function to include three new test cases.
# These should assert that hand_rank gives the appropriate
# output for the given straight flush, four of a kind, and
# full house.
# For example, calling hand_rank on sf should output (8, 10)
# Modify the test() function to include three new test cases.
# These should assert that card_ranks gives the appropriate
# output for the given straight flush, four of a kind, and
# full house.
#
# For example, calling card_ranks on sf should output
# [10, 9, 8, 7, 6]


# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

import random


# this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

my_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=my_deck):
    # Your code here.
    random.shuffle(deck)
    player_hands = {i: [] for i in range(numhands)}
    for player in range(numhands):
        for num_cards in range(n):
            player_hands[player].append(deck.pop())
    return player_hands

"""
optimized solution:
def deal(numhands, n, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Shuffle the deck and deal out numhands n-card hands"
    # n: number of cards
    # numhands: number of players
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)] # take cards in sequential

print(deal(2,7))
"""
hand_names = ["Straight Flush", "4 kind", "Full House", "Flush",
              "Straight", "3 kind", "2 pair", "Pair", "high card"]

def hand_percentage(n=700*000):
    """Sample n random hands and print a table of percentages for each type of hand"""
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print("%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n))


def test():
    """Test cases for the functions in poker program"""
    sf1 = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC'] (T means 10) straight flush
    sf2 = "6D 7D 8D 9D TD".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
    assert poker([sf1, fk, fh]) == sf1
    # Add 2 new assert statements here. The first
    # should check that when fk plays fh, fk
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    # Add 2 new assert statements here. The first
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second
    # should check for the case of 100 hands.
    assert poker([sf1]) == sf1
    assert poker([sf1] + 99*[fh]) == sf1

    # add 3 new assert statements here.
    assert hand_rank([sf1]) == (8, 10)
    assert hand_rank([fk]) == (7, 9, 7)
    assert hand_rank([fh]) == (6, 10, 7)
    assert card_ranks(sf1) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf1) == True
    assert flush(fk) == False
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert straight(card_ranks(al)) == True
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    return 'tests pass'


print(test())


