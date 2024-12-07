from time import time
import itertools

def parse_input():
    equations = []
    with open('input.txt') as f:
        lines = f.readlines()
    equations = [list(map(int,line.strip().replace(':','').split(' '))) for line in lines]
    return equations

def part1(puzzle):
    counter = 0
    ops = ['+', '*']
    for equation in puzzle:
        counter += try_equation(equation, ops)
    return counter

def part2(puzzle):
    counter = 0
    ops = ['+', '*', '||']
    for equation in puzzle:
        counter += try_equation(equation, ops)
    return counter

def try_equation(equation, ops):
    sum = equation[0]
    num_ops = len(equation)-2
    op_combinations = itertools.product(ops, repeat=num_ops)
    for combination in op_combinations:
        result = equation[1]
        for i, op, in enumerate(combination):
            if op == '+':
                result += equation[i+2]
            elif op == '*':
                result *= equation[i+2]
            else:
                result = int(str(result)+str(equation[i+2]))
        if result == sum:
            return sum
    return 0

def solve():
    puzzle = parse_input()
    print(part1(puzzle))
    print(part2(puzzle))


def get_answer():
    start_time = time()
    solve()
    print("puzzle took", time() - start_time)

if __name__ == "__main__":
    get_answer()