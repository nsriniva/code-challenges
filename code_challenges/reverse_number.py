
def rev_num(n):
    n_str = str(n)
    revn_str = n_str[-1::-1]

    ret = int(revn_str)

    return ret


from collections import Counter

def most_freq(l):
    lcount = Counter(l)

    slcount = sorted(lcount.items(), reverse=True, key= lambda x: x[1])

    return slcount[0][0]

test_vec_rev = [
    (1234,4321),
    (1209,9021)
]

test_vec_mfreq = [
    ([1,2,2,5,6,5,4,5,3,7], 5)
]
    
if __name__ == '__main__':

    for tv in test_vec_rev:
        assert rev_num(tv[0]) == tv[1]

    for tv in test_vec_mfreq:
        assert most_freq(tv[0]) == tv[1]
