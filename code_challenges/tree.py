class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from itertools import chain


# Breadth first traversal of binary tree
def tree_from_list(l, i=0):

    nl = deque()

    ll = len(l)

    node = TreeNode(l[i])
    i += 1

    nl.appendleft(node)

    while len(nl):
        n = nl.pop()

        if i < ll:
            if l[i] is not None:
                n.left = TreeNode(l[i])
                nl.appendleft(n.left)
            i += 1
            if i < ll:
                if l[i] is not None:
                    n.right = TreeNode(l[i])
                    nl.appendleft(n.right)
                i += 1

    return node


def trim_breadth_first_list(bf_list):
    # Locate index of first non null(None) node val
    # searching backward from the end of list
    for idx, e in enumerate(bf_list[-1::-1]):
        # print(idx,e)
        if e is not None:
            break
    # print(idx)
    # Remove all trailing null(None) values from out
    return bf_list[:-idx]


def list_from_tree(tree):
    q = deque()

    q.appendleft(tree)

    out = []

    while len(q):

        nd = q.pop()

        if nd is None:
            out.append(None)
        else:
            out.append(nd.val)
            q.appendleft(nd.left)
            q.appendleft(nd.right)

    return trim_breadth_first_list(out)


# Breadth first traversal with each level in a sub list
def list_of_lists_from_tree(tree):
    q = deque()

    q.appendleft((tree, 1))

    out = []

    currlvl = 1
    currl = []

    while len(q):

        nd, l = q.pop()
        if l > currlvl:
            out.append(currl)
            currlvl = l
            currl = []

        if nd is None:
            currl.append(None)
        else:
            currl.append(nd.val)
            q.appendleft((nd.left, currlvl + 1))
            q.appendleft((nd.right, currlvl + 1))

    out.append(currl)
    return out


null = None

test_vec = [
    ([2, 1, 3], True),
    ([5, 1, 4, null, null, 3, 6], False),
    ([5, 4, 6, null, null, 3, 7], False),
    ([1, 1], False),
    ([0, -1], True),
    ([32, 26, 47, 19, null, null, 56, null, 27], False),
    ([5, 14, null, 1], False),
    ([120, 70, 140, 50, 100, 130, 160, 20, 55, 75, 110, 119, 135, 150, 200], False),
    ([3, 1, 5, 0, 2, 4, 6], True),
    ([3, null, 30, 10, null, null, 15, null, 45], False),
]


def rec_valid(root):

    l = root.left
    r = root.right

    ret = [root.val, root.val]

    if r:
        if (rret := rec_valid(r)) is not None:
            if rret[0] <= root.val:
                return None
            ret[1] = rret[1]
        else:
            return None

    if l:
        if (lret := rec_valid(l)) is not None:
            if lret[1] >= root.val:
                return None
            ret[0] = lret[0]
        else:
            return None

    # print(ret)
    return ret


def validBST(root: TreeNode) -> bool:

    ret = rec_valid(root)

    return ret is not None


for l in test_vec:
    t = tree_from_list(l[0])
    lp = list_from_tree(t)
    assert l[0] == lp

    llp = list_of_lists_from_tree(t)
    lp = trim_breadth_first_list(list(chain(*llp)))
    assert l[0] == lp

    assert l[1] == validBST(t)

kl = [
    45,
    30,
    46,
    10,
    36,
    null,
    49,
    8,
    24,
    34,
    42,
    48,
    null,
    4,
    9,
    14,
    25,
    31,
    35,
    41,
    43,
    47,
    null,
    0,
    6,
    null,
    null,
    11,
    20,
    null,
    28,
    null,
    33,
    null,
    null,
    37,
    null,
    null,
    44,
    null,
    null,
    null,
    1,
    5,
    7,
    null,
    12,
    19,
    21,
    26,
    29,
    32,
    null,
    null,
    38,
    null,
    null,
    null,
    3,
    null,
    null,
    null,
    null,
    null,
    13,
    18,
    null,
    null,
    22,
    null,
    27,
    null,
    null,
    null,
    null,
    null,
    39,
    2,
    null,
    null,
    null,
    15,
    null,
    null,
    23,
    null,
    null,
    null,
    40,
    null,
    null,
    null,
    16,
    null,
    null,
    null,
    null,
    null,
    17,
]


def kthSmallest(root, k):
    n = 0
    if root.left:
        n, s = kthSmallest(root.left, k)

    if n < k:
        n += 1
        s = root.val

    if n < k and root.right:
        nt, s = kthSmallest(root.right, k - n)
        n += nt

    return n, s


k_tree = tree_from_list(kl)


def inorder(root):
    ret = []
    if root.left:
        ret = inorder(root.left)
    ret.append(root.val)
    if root.right:
        ret += inorder(root.right)

    return ret


inorder_list = inorder(k_tree)
# print(inorder_list)

for idx, e in enumerate(inorder_list):
    n, s = kthSmallest(k_tree, idx + 1)
    # print(idx, e, n, s)
    assert n == idx + 1 and s == e


def build_tree(preorder, inorder):

    root = preorder[0]
    idx = inorder.index(root)

    ret = TreeNode(root)

    li = inorder[:idx]
    ri = inorder[idx + 1 :]

    if lli := len(li):
        ret.left = build_tree(preorder[1 : 1 + lli], li)
    if len(ri):
        ret.right = build_tree(preorder[1 + lli :], ri)

    return ret


preorder = [5, 7, 22, 13, 9]
inorder = [7, 5, 13, 22, 9]
bflist = [5, 7, 22, null, null, 13, 9]

ret = build_tree(preorder, inorder)

l = list_from_tree(ret)

assert bflist == l
