#
# Your previous Python 3 content is preserved below:
#
# /**
# Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root. For example, boundary traversal of the following tree
#
#                   20
#                 /    \
#                8     22
#              /   \     \
#             4    12     25
#                 /  \     \
#                10  14    27
#
# is “20 8 4 10 14 27 25 22”
#
# e.g 2:
#             1
#              \
#               2
#              / \
#             3   4
#
# Output is: "1 3 4 2"
# */
#
# class TreeNode {
#   int val;
#   TreeNode left;
#   TreeNode right;
#   TreeNode() {}
#
#   TreeNode(int val) { this.val = val; }
#
# }
#

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree():
    n4 = TreeNode(4)
    n8 = TreeNode(8)
    n20 = TreeNode(20)
    n12 = TreeNode(12)
    n10 = TreeNode(10)
    n14 = TreeNode(14)
    n22 = TreeNode(22)
    n25 = TreeNode(25)
    n27 = TreeNode(27)

    n20.left = n8
    n20.right = n22
    n8.left = n4
    n8.right = n12
    n12.left = n10
    n12.right = n14
    n22.right = n25
    n25.right = n27

    return n20


def get_border(tree):
    q = deque()

    q.appendleft((tree, 1))

    border_left = []
    border_right = deque()

    currlvl = 1
    currl = []

    while len(q):

        nd, l = q.pop()
        if l > currlvl:
            border_left.append(currl[0])
            border_right.appendleft(currl[-1])
            currlvl = l
            currl = []

        currl.append(nd.val)
        if nd.left is not None:
            q.appendleft((nd.left, currlvl + 1))
        if nd.right is not None:
            q.appendleft((nd.right, currlvl + 1))

    # The root level list has just 1 element which is (left)appended to both
    # norder_right and border_left lists - so we ignore the last element in
    # border_right
    return border_left + currl + list(border_right)[:-1]


print(border := get_border(create_tree()))

border_correct = [20, 8, 4, 10, 14, 27, 25, 22]

assert border == border_correct
