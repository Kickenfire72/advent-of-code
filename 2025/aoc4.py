from utils import *

def load_matrix(path: str):
    matrix = []
    with open(path, "r") as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

def g(i, j, matrix):
    if (i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i])):
        return 0
    elif matrix[i][j] == '.':
        return 0
    else:
        return 1

def goOnce(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            rolls = g(i - 1, j - 1, m) + g(i - 1, j, m) + g(i - 1, j + 1, m) + g(i, j - 1, m) + g(i, j + 1, m) + g(
                i + 1, j - 1, m) + g(i + 1, j, m) + g(i + 1, j + 1, m)
            isRemovable = 1 if rolls < 4 and m[i][j] == "@" else 0
            count += isRemovable
            if isRemovable == 1:
                m[i][j] = '.'
    return count

def part1(filename):
    m = load_matrix(filename)
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            rolls = g(i - 1, j - 1, m) + g(i - 1, j, m) + g(i - 1, j + 1, m) + g(i, j - 1, m) + g(i, j + 1, m) + g(
                i + 1, j - 1, m) + g(i + 1, j, m) + g(i + 1, j + 1, m)
            count += 1 if rolls < 4 and m[i][j] == "@" else 0
    print(count)

def part2(filename):
    m = load_matrix(filename)
    oneCount = 1
    totalCount = 0
    while oneCount != 0:
        oneCount = goOnce(m)
        totalCount += oneCount
    print(totalCount)

if __name__ == "__main__":
    start(4, part1, part2)