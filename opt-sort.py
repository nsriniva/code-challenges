def sort_list(inp: list) -> list:
    inp.sort()
    return inp


test_vecs = [
    ([10, 5, 1, 7, 40, 50], [1, 5, 7, 10, 40, 50]),
]

if __name__ == "__main__":
    for tv in test_vecs:
        assert tv[1] == sort_list(tv[0])
