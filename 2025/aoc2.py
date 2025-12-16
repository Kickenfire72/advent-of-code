from utils import *

def load_ranges(path: str) -> list[list[str]]:
    with open(path, 'r', encoding='utf-8') as f:
        return [range.split("-") for range in f.readline().rstrip('\n').split(",")]

def part1(filename):
    ranges: list[list[str]] = load_ranges(filename)
    total = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            id = str(i)
            half = len(id) // 2
            if id[0:half] == id[half:]:
                total += i
    print(total)

def part2(filename):
    ranges: list[list[str]] = load_ranges(filename)
    total = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            id = str(i)
            l = len(id)
            cond = 0
            for k in range(1, l // 2 + 1):
                if l % k == 0 and id == id[:k] * (l // k):
                    cond += 1
            if cond > 0:
                total += i
    print(total)

if __name__ == "__main__":
    start(2, part1, part2)
