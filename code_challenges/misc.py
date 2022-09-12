from collections import defaultdict


def checkBlanagrams1(word1, word2):

    if len(word1) != len(word2):
        return False

    ld = defaultdict(int)
    for w in word1:
        ld[w] += 1
    for w in word2:
        ld[w] -= 1

    lcd = defaultdict(int)
    for lc in ld.values():
        lcd[lc] += 1

    return len(lcd) <= 3 and lcd[-1] == 1 and lcd[1] == 1


def checkBlanagrams2(word1, word2):

    if len(word1) != len(word2):
        return False

    ld = defaultdict(int)
    for w in word1:
        ld[w] += 1
    for w in word2:
        ld[w] -= 1

    lcd = [0] * 3
    for lc in ld.values():
        i = lc + 1
        # We only expect counts of -1(0), 0(1) or 1(2)
        if i > 2 or i < 0:
            return False
        lcd[i] += 1

    return lcd[0] == 1 and lcd[2] == 1


def findValueSortedShiftedArray(nums, target):
    ln = len(nums)

    s = 0
    e = ln - 1

    while s <= e:
        m = (s + e) // 2
        if target == nums[m]:
            return m
        if target < nums[m]:
            if nums[s] <= target:
                e = m - 1
            else:
                s = m + 1
        else:
            if nums[e] >= target:
                s = m + 1
            else:
                e = m - 1

    return -1


def reverseLinkedList(l):

    prev = None
    curr = l

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def csBSTRangeSum(root, lower, upper):

    ret = 0

    if root is not None:
        ret += csBSTRangeSum(root.left, lower, upper)
        if root.value >= lower and root.value <= upper:
            ret += root.value
        ret += csBSTRangeSum(root.right, lower, upper)

    return ret


def csBinaryTreeInvert(root):

    if root is not None:
        r = root.right

        root.right = csBinaryTreeInvert(root.left)
        root.left = csBinaryTreeInvert(r)

    return root
