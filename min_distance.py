def hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def get_min_hamming(array):
    min = len(array)
    for i in array:
        for j in array:
            if i is j:
                continue
            if hamming(i, j) < min:
                min = hamming(i, j)

    return min


inputs = []
while True:
    inp = raw_input("Input strings:")
    if inp == "":
        break
    inputs.append(inp)

print("Minimum:" + str(get_min_hamming(inputs)))
