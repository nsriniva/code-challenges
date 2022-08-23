from typing import Optional


class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def add_to_link_list(new_node: int, inp: Optional[Node]) -> Node:
    nnode = Node(new_node)
    nnode.next = inp
    return nnode


test_vecs = [
    ((10, 15, 20, 25), 5, (5, 10, 15, 20, 25)),
]


if __name__ == "__main__":
    for tv in test_vecs:
        assert (ltv0 := len(tv[0])) > 0
        assert ltv0 + 1 == len(tv[2])

        a = None
        for ae in tv[0][::-1]:
            a = add_to_link_list(ae, a)

        a = add_to_link_list(tv[1], a)

        n = a
        idx = 0
        while n is not None:
            assert n.val == tv[2][idx]
            idx += 1
            n = n.next
