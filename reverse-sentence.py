def rev_sentence(inp : str) -> str:

    ilist = inp.split()

    return ' '.join(ilist[::-1])


test_vecs = [
    ('sun rises in the east', 'east the in rises sun'),
    ]


if __name__ == '__main__':
    for tv in test_vecs:
        assert tv[1] == rev_sentence(tv[0])
