def check_cuts(minLength: int, lengths: list) -> bool:

    llen = len(lengths)
    slen = sum(lengths)

    if llen < 2:
        return False

    if llen == 2 and slen >= minLength:
        return True

    ret = check_cuts(minLength, lengths[1:])

    if ret == False:
        ret = check_cuts(minLength, lengths[: llen - 1])

    return ret


test_vecs = [
    (7, (4, 3, 2), True),
    (7, (4, 3), True),
    (7, (4, 2, 3), False),
    (7, (4, 3, 2, 3), True),
    (7, (3, 2, 3, 4), True),
    (7, (3, 2, 3, 3), False),
]

if __name__ == "__main__":
    for tv in test_vecs:
        assert check_cuts(tv[0], tv[1]) == tv[2]
