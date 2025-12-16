from utils import *
from math import *
from itertools import combinations
from collections import Counter

def load_points(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        list = []
        for line in f:
            l = line.rstrip('\n').split(',')
            list.append((int(l[0]), int(l[1])))
        return list

def all_pairs(l):
    combs = list(combinations(range(len(l)), 2))
    return combs

def get_area(points, pair):
    return (abs(points[pair[0]][1]-points[pair[1]][1])+1)*(abs(points[pair[0]][0]-points[pair[1]][0])+1)

def part1(filename):
    points = load_points(filename)
    pairs = all_pairs(points)
    areas = list(map(lambda pair: get_area(points, pair), pairs))
    print(max(areas))

def part2(filename):
    return 0

if __name__ == "__main__":
    start(9, part1, part2)
