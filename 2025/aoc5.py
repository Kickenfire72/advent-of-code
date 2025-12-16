from utils import *

def load_data(path: str):
    with open(path) as f:
        validIdRangeLines, idLines = (part.splitlines() for part in f.read().strip().split("\n\n"))
        validIdRanges = [list(map(int, line.split("-"))) for line in validIdRangeLines]
        ids = list(map(int, idLines))
    return validIdRanges, ids

def part1(filename):
    validIdRanges, ids = load_data(filename)
    count = 0
    for id in ids:
        exists = False
        j = 0
        while exists == False and j < len(validIdRanges):
            exists = (id >= validIdRanges[j][0] and id <= validIdRanges[j][1])
            j += 1
        count += exists
    print(count)

def part2(filename):
    validIdRanges, ids = load_data(filename)
    validIdRanges.sort(key=lambda x: x[0])

    def badi(list):
        i = 0
        while i < len(list) - 2 and list[i][1] < list[i + 1][0]:
            i = i + 1
        if i > len(list) - 2 or list[i][1] < list[i + 1][0]:
            return -1
        else:
            return i

    k = badi(validIdRanges)
    while k < len(validIdRanges) - 1 and k != -1 and k != -2:
        a = validIdRanges.pop(k)
        b = validIdRanges.pop(k)
        smol = a + b
        smol.sort()
        validIdRanges.append([smol[0], smol[-1]])
        validIdRanges.sort(key=lambda x: x[0])
        k = badi(validIdRanges)
    counts = list(map(lambda k: k[1] - k[0] + 1, validIdRanges))
    print(sum(counts))

if __name__ == "__main__":
    start(5, part1, part2)
