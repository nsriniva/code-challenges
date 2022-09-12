# Hand of 5 (6 sided - die)
# 1 1 2 3 4 -> 1 pair
# 1 1 2 2 3 -> two pair
# 1 2 3 4 5 -> straight
# 1 2 3 3 3 -> 3 of a kind
# 1 1 2 2 2 -> full house - 1 2 1 2 2
# 2 2 2 2 1 -> 4 of a kind
# all other cases -> other

from collections import Counter

FOUR_OF_A_KIND = "4 of a kind"
FULL_HOUSE = "full house"
THREE_OF_A_KIND = "3 of a kind"
STRAIGHT = "straight"
TWO_PAIR = "2 pair"
ONE_PAIR = "1 pair"
OTHER = "other"


def classifier(hand):
    cntr = Counter(hand)

    pairs = 0
    triple = 0
    quad = 0
    singles = 0
    for e in cntr.keys():
        if cntr[e] == 2:
            pairs += 1
        elif cntr[e] == 3:
            triple += 1
        elif cntr[e] == 4:
            quad += 1
        else:
            singles += 1

    rpairs = [ONE_PAIR, TWO_PAIR]
    if quad:
        return FOUR_OF_A_KIND
    if triple:
        if pairs:
            return FULL_HOUSE
        else:
            return THREE_OF_A_KIND
    if pairs:
        return rpairs[pairs - 1]

    hsum = sum(hand)
    if singles == 5 and (hsum == 15 or hsum == 20):
        return STRAIGHT

    return OTHER


test_vecs = [
    ([1, 1, 2, 3, 4], ONE_PAIR),
    ([1, 1, 2, 2, 3], TWO_PAIR),
    ([1, 2, 3, 4, 5], STRAIGHT),
    ([1, 2, 3, 3, 3], THREE_OF_A_KIND),
    ([1, 1, 2, 2, 2], FULL_HOUSE),
    ([2, 2, 2, 2, 1], FOUR_OF_A_KIND),
    ([1, 1, 1, 1, 1], "other"),
    ([1, 2, 1, 2, 2], FULL_HOUSE),
    ([2, 3, 4, 5, 6], STRAIGHT),
]

for t in test_vecs:
    print(f"Testing {t[0]} - expecting {t[1]}")
    assert classifier(t[0]) == t[1]
