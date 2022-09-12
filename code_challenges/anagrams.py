from collections import defaultdict


def pal_check(words):

    pald = defaultdict(list)

    for word in words:
        ws = "".join(sorted(word))

        pald[ws].append(word)

    return list(pald.values())


testvec = [(["cat", "act", "tac", "jam"], [["cat", "act", "tac"], ["jam"]])]

for t in testvec:
    assert pal_check(t[0]) == t[1]
