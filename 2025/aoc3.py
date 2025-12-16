from utils import *

def load_lines(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def getDigitAndIndex(big, count, maxDigit):
    idx = big.find(str(maxDigit))
    if count == 0:
        return ""
    elif idx < len(big)-count+1 and idx != -1:
        return str(maxDigit) + getDigitAndIndex(big[idx+1:], count-1, 9)
    else:
        return getDigitAndIndex(big, count, maxDigit-1)

def part1(filename):
    lines: list[str] = load_lines(filename)
    total = 0
    for line in lines:
        total += max([max([int(line[i] + j) for j in line[i + 1:]]) for i in range(len(line) - 1)])
    print(total)

def part2(filename):
    lines: list[str] = load_lines(filename)
    total = 0
    for line in lines:
        line = int(getDigitAndIndex(line, 12, 9))
        total += line
    print(total)

if __name__ == "__main__":
    start(3, part1, part2)
