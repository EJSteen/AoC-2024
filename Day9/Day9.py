from time import time
import copy

def parse_input():
    with open('input.txt') as f:
        line = [int(x) for x in list(f.readline().strip())]
    return line

def part1(fs):
    counter = 0
    new_fs = copy.deepcopy(fs)
    for i in range(len(fs)-1):
        if fs[i] == -1 and len(new_fs) > i:
            new_fs[i] = new_fs[len(new_fs)-1]
            new_fs.pop()
            while new_fs[len(new_fs)-1] == -1:
                new_fs.pop()
    for i, block in enumerate(new_fs):
        counter += i * block
    return counter

def part2(fs):
    counter = 0
    new_fs = copy.deepcopy(fs)
    blocks = get_blocks(fs)
    free_spaces = []
    for block in blocks:
        print(block[0])
        fs = new_fs
        for i in range(len(fs)-1):
            if i > new_fs.index(block[0]):
                free_spaces.clear()
                break
            if fs[i] == -1:
                free_spaces.append(i)
            elif len(free_spaces) > 0:
                if len(free_spaces) >= block[1]:
                    new_fs = [-1 if x==block[0] else x for x in new_fs]
                    for i in range(block[1]):
                        new_fs[free_spaces[i]] = block[0]
                    free_spaces.clear()
                    break
                free_spaces.clear()
    for i, block in enumerate(new_fs):
        if block != -1:
            counter += i * block
    return counter, new_fs

def get_blocks(fs):
    blocks = []
    fs = list(filter(lambda a: a != -1, fs))
    while len(fs) > 0:
        current_id = fs[len(fs)-1]
        fs.pop()
        space = 1
        while len(fs) > 1 and fs[len(fs)-1] == current_id:
            space += 1
            fs.pop()
        blocks.append((current_id, space))
    return blocks
    

def get_fs(line):
    fs = []
    id = 0
    for i, num in enumerate(line):
        if i % 2 == 0:
            for j in range(num):
                fs.append(id)
            id += 1
        else:
            for j in range(num):
                fs.append(-1)
    return fs         

def solve():
    puzzle = parse_input()
    fs = get_fs(puzzle)
    #print("Part 1:",part1(fs))
    print("Part 2:",part2(fs))

def get_answer():
    start_time = time()
    solve()
    print("puzzle took", time() - start_time)

if __name__ == "__main__":
    get_answer()