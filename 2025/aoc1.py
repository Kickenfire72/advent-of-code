from utils import *

def load_lines(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def part1(filename):
    lines: list[str] = load_lines(filename)
    dot = 50
    passwd = 0
    for line in lines:
        dot = (dot + (1 if line[0] == 'R' else -1) * int(line[1:])) % 100
        passwd += 1 if dot == 0 else 0
    print(passwd)

def part2(filename):
    lines: list[str] = load_lines(filename)
    dot = 50
    passwd = 0
    for line in lines:
        newdot = (dot + (1 if line[0] == 'R' else -1) * int(line[1:]))
        passwd += abs(newdot // 100)
        dot = newdot % 100
    print(passwd)

if __name__ == "__main__":
    start(1, part1, part2)
