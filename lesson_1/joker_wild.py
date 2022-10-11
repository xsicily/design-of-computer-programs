# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. 
# The black joker, '?B', can be used as any spade or club and
# the red joker, '?R', can be used as any heart
# or diamond.
#
# The itertools library may be helpful. Feel free to
# define multiple functions if it helps you solve the
# problem.
#
# -----------------
# Grading Notes
#
# Muliple correct answers will be accepted in cases
# where the best hand is ambiguous (for example, if
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

# Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color.
rank_options = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
# The black joker, '?B', can be used as any spade (S) or club (C)
joker_b = [''.join(i) for i in list(itertools.product(rank_options, ['S', 'C']))]
# The red joker, '?R', can be used as any heart (H) or diamond (D)
joker_r = [''.join(i) for i in list(itertools.product(rank_options, ['H', 'D']))]

"""
optimized solution:

joker_b = [rank + suit for rank in "23456789TJQKA" for suit in ['S','C']]
joker_r = [rank + suit for rank in "23456789TJQKA" for suit in ['H','D']]

"""

# How to replace the joker???
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    # Your code here
    hand_no_joker =[]
    joker = []
    if joker_or_not(hand):
        hand_no_joker = [[item for item in hand if not '?' in item]]
        joker = [item for item in hand if '?' in item]
        joker_choice = []
        if len(joker) == 1:
            joker_choice = [x.split() for x in joker_replace(joker)]
        elif len(joker) == 2:
            # all the combination of the replacement of black joker and red joker
            joker_choice = [list(item) for item in list(itertools.product(joker_replace([joker[0]]), joker_replace([joker[1]])))]
        # List all the combinations in nested list between hand without joker and joker replacement
        hands_choice = [list(item) for item in list(itertools.product(hand_no_joker, joker_choice))]
        # Merge the hand without joker and joker replacement into one new hand
        hands_new = [a+b for a,b in hands_choice]
        # get the best hand for each new hand
        best_hands_list = [best_hand(hand) for hand in hands_new]
        return max(best_hands_list, key = hand_rank)
    return best_hand(hand)


def joker_replace(card):
    """input card (type: string list) and output the possible joker replacement"""
    if card == ['?B']: 
        return joker_b
    elif card == ['?R']: 
        return joker_r
    else: 
        return card

def joker_or_not(hand):
    """Boolean function to evaluate the joker
    -has joker, return True
    -no joker, return False
    """
    if '?B' in hand or '?R' in hand:
        return True
    return False

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    # Your code here
    return max(list(itertools.combinations(hand,5)), key = hand_rank)


# ------------------
# Provided Functions
#
# You may want to use some of the functions which
# you have already defined in the unit to write
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight(ranks):
    """Return True if the ordered
    ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def kind(n, ranks):
    """Return the first rank that this hand has
    exactly n-of-a-kind of. Return None if there
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None


def two_pair(ranks):
    """If there are two pair here, return the two
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

print(test_best_wild_hand())