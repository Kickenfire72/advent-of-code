from utils import *

def load_matrix(path: str):
    matrix = []
    with open(path, "r") as f:
        for line in f:
            matrix.append(line.strip())
    return matrix

def number_under(m, i, j, splitters):
    currenti = i
    while currenti < len(m)-1 and m[currenti][j] != "^":
        currenti += 1
    points = list(map(lambda e: e[0], splitters))
    if currenti == len(m)-1:
        return 1
    elif m[currenti][j] == "^" and (currenti, j) in points:
        loc = points.index((currenti, j))
        return splitters[loc][1] # this is under
    elif m[currenti][j] == "^" and not (currenti, j) in points:
        left_count = number_under(m, currenti, j - 1, splitters)
        right_count = number_under(m, currenti, j + 1, splitters)
        under = left_count + right_count
        splitters.append(((currenti, j), under))
        return under

def check(m, i, j, splitters):
    currenti = i
    while currenti < len(m)-1 and m[currenti][j] != "^":
        currenti += 1
    if m[currenti][j] == "^" and not (currenti, j) in splitters:
        splitters.append((currenti, j))
        check(m, currenti, j-1, splitters)
        check(m, currenti, j+1, splitters)

def part1(filename):
    matrix = load_matrix(filename)
    splitters = []
    slocation = matrix[0].index("S")
    check(matrix, 0, slocation, splitters)
    count = len(list(set(splitters)))
    print(count)

def part2(filename):
    matrix = load_matrix(filename)
    splitters = []
    slocation = matrix[0].index("S")
    number_under(matrix, 0, slocation, splitters)
    count = splitters[-1][1]
    print(count)

if __name__ == "__main__":
    start(7, part1, part2)