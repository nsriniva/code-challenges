from heapq import heappush, heappop, heapreplace


def solve(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    minh = []
    n = 0
    l = len(A)

    i = 0
    while i < l:
        j = 0
        while j < l:
            s = A[i] + B[j]
            if n < l:
                heappush(minh, s)
                n += 1
            elif s > minh[0]:
                heapreplace(minh, s)
            elif s <= minh[0]:
                break
            j += 1

        if j == 0:
            break

        i += 1
        index = index - (index & (-index))
    i = 0

    v = []
    while i < l:
        v.insert(0, heappop(minh))
        i += 1

    return v
