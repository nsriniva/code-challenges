from string import ascii_letters


def rev_str(istr):

    print(istr, len(istr))
    ostr = []
    tstr = ""
    for i in istr:

        if i in ascii_letters:
            tstr += i
            continue

        if len(tstr) > 0:
            ostr.append(tstr)
            tstr = ""

        if i != " ":
            # Store end char
            endc = i
            break

    ostr = ostr[-1::-1]

    ostr[-1] += endc
    print(ostr)

    ret = " ".join(ostr).capitalize()
    return ret


test_vecs = [
    ("  Wow  mom!  ", "Mom wow!"),
]


for tv in test_vecs:
    assert rev_str(tv[0]) == tv[1]
