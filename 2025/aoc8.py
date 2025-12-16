from utils import *
from math import *
from itertools import combinations
from collections import Counter

def load_points(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        list = []
        for line in f:
            l = line.rstrip('\n').split(',')
            list.append((int(l[0]), int(l[1]), int(l[2])))
        return list

def get_dist(l, c):
    return sqrt((l[c[0]][0] - l[c[1]][0]) ** 2 + (l[c[0]][1] - l[c[1]][1]) ** 2 + (l[c[0]][2] - l[c[1]][2]) ** 2)

def smallest_dists(l, count):
    combs = list(combinations(range(len(l)), 2))
    sorts = sorted(combs, key=lambda c: get_dist(l, c))
    return sorts[:count]

def all_dists(l):
    combs = list(combinations(range(len(l)), 2))
    sorts = sorted(combs, key=lambda c: get_dist(l, c))
    return sorts

def part1(filename):
    points = load_points(filename)
    pairs = smallest_dists(points, 1000)
    groups = len(points)*[0]
    new_group = 1
    for i in range(len(pairs)):
        pair = pairs[i]
        if groups[pair[0]] == 0 and groups[pair[1]] == 0:
            groups[pair[0]] = new_group
            groups[pair[1]] = new_group
            new_group += 1
        elif groups[pair[0]] != 0 and groups[pair[1]] == 0:
            groups[pair[1]] = groups[pair[0]]
        elif groups[pair[1]] != 0 and groups[pair[0]] == 0:
            groups[pair[0]] = groups[pair[1]]
        elif groups[pair[0]] != 0 and groups[pair[1]] != 0 and groups[pair[0]] != groups[pair[1]]:
            group1 = groups[pair[0]]
            group2 = groups[pair[1]]
            for k in range(len(groups)):
                if groups[k] == group1 or groups[k] == group2:
                    groups[k] = new_group
            new_group += 1
    counts = Counter(groups)
    del counts[0]
    nums = sorted(counts.values(), reverse=True)
    print(nums[0]*nums[1]*nums[2])

# Part 2 was surprisingly easy after doing part 1
def part2(filename):
    points = load_points(filename)
    pairs = all_dists(points)
    groups = len(points) * [0]
    new_group = 1
    i = 0
    conn_count = len(points)
    while i < len(pairs) and conn_count != 1:
        pair = pairs[i]
        if groups[pair[0]] == 0 and groups[pair[1]] == 0:
            groups[pair[0]] = new_group
            groups[pair[1]] = new_group
            new_group += 1
        elif groups[pair[0]] != 0 and groups[pair[1]] == 0:
            groups[pair[1]] = groups[pair[0]]
        elif groups[pair[1]] != 0 and groups[pair[0]] == 0:
            groups[pair[0]] = groups[pair[1]]
        elif groups[pair[0]] != 0 and groups[pair[1]] != 0 and groups[pair[0]] != groups[pair[1]]:
            group1 = groups[pair[0]]
            group2 = groups[pair[1]]
            for k in range(len(groups)):
                if groups[k] == group1 or groups[k] == group2:
                    groups[k] = new_group
            new_group += 1
        counts = Counter(groups)
        conn_count = len(counts.keys())
        i += 1
    final_pair = pairs[i-1]
    print(points[final_pair[0]][0]*points[final_pair[1]][0])

if __name__ == "__main__":
    start(8, part1, part2)