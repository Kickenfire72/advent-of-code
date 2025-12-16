from utils import *
from functools import reduce

def load_matrix(path: str):
    matrix = []
    with open(path, "r") as f:
        for line in f:
            matrix.append(line.strip().split())
    return matrix

def load_matrix_2(path: str):
    matrix = []
    with open(path, "r") as f:
        for line in f:
            matrix.append(line)
    t = [list(row) for row in zip(*matrix)]
    newt = ["".join(line) for line in t]
    newt = newt[:-2]

    result = []
    current = []
    for x in newt:
        if x.strip() == "":
            result.append(current)
            current = []
        else:
            current.append(x.strip())
    result.append(current)

    for problem in result:
        first = problem.pop(0)
        problem.append(first[:-1].strip())
        problem.append(first[-1])
    return result

def read_value(lines, i):
    value = ""
    for k in range(len(lines)-1):
        if lines[k][i] != "":
            if i >= len(lines[k]):
                value += ""
            else:
                value += lines[k][i]
    return value.strip()

def load_matrix_3(path: str):
    lines = []
    with open(path, "r") as f:
        for line in f:
            lines.append(line)
    problems = []
    new_problem = [""]
    value = ""
    for i in range(len(lines[0])):
        if value == "":
            if new_problem[-1] == "":
                new_problem.pop(-1)
            problems.append(new_problem)
            new_problem = []
            new_problem.append(lines[-1][i])
            value = read_value(lines, i)
            new_problem.append(value)
        else:
            value = read_value(lines, i)
            new_problem.append(value)
    if new_problem[-1] == "":
        new_problem.pop(-1)
    problems.append(new_problem)
    return problems

def pick_operation(operation_string):
    match operation_string:
        case "+":
            return lambda a,b: a+b, 0
        case "*":
            return lambda a,b: a*b, 1

def solve_problem(problem):
    op, acc = pick_operation(problem[-1])
    return reduce(op, map(int, problem[:-1]), acc)

def solve_problem_2(problem):
    op, acc = pick_operation(problem[0])
    return reduce(op, map(int, problem[1:]), acc)

def part1(filename):
    m = load_matrix(filename)
    t = [list(row) for row in zip(*m)]
    totals = [solve_problem(problem) for problem in t]
    print(sum(totals))

def part2(filename):
    m = load_matrix_3(filename)
    m.pop(0)
    totals = [solve_problem_2(problem) for problem in m]
    print(sum(totals))

if __name__ == "__main__":
    start(6, part1, part2)
