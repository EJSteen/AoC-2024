import re

def parse_input(part1):
    muls = []
    with open('input.txt') as f:
        if (part1):
            muls = re.findall(r"mul\(\d+,\d+\)", f.read())
        else:
            muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", f.read())
    return muls

def part1():
    muls = parse_input(True)
    total = 0
    for mul in muls:
        digs = re.findall(r"\d+", mul)
        total += int(digs[0]) * int(digs[1])
    return total

def part2():
    muls = parse_input(False)
    total = 0
    on = True
    for mul in muls:
        if (mul == "don't()"):
            on = False
        elif (mul == "do()"):
            on = True
        elif (on):
            digs = re.findall(r"\d+", mul)
            total += int(digs[0]) * int(digs[1])
    return total


def get_answer():
    print(part1(), part2())

if __name__ == "__main__":
    get_answer()