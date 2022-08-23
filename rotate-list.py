from collections import deque


def rotate_list(inp: list) -> list:

    ideque = deque(inp)

    o = ideque.pop()
    ideque.appendleft(o)

    return list(ideque)


test_vecs = [
    ([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]),
]

if __name__ == "__main__":
    for tv in test_vecs:
        assert tv[1] == rotate_list(tv[0])
