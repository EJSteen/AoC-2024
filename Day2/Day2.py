def parse_input():
    levels = []
    with open('input.txt') as f:
        for line in f:
            levels += [[int(x) for x in line.strip().split(' ')]]
    return levels

def part1():
    levels = parse_input()
    counter = 0
    for level in levels:
        if is_safe(level):
            counter += 1
    return counter

def is_safe(level):
    if level == sorted(level) or level == sorted(level, reverse=True):
            print(level)
            safe = True
            for i in range(len(level)-1):
                diff = abs(int(level[i]) - int(level[i+1]))
                if diff > 3 or diff < 1:
                    print(level[i],level[i+1])
                    safe = False
                    break
            if safe:
                return True
    return False
    

def part2():
    levels = parse_input()
    counter = 0
    for level in levels:
        if is_safe(level):
            counter += 1
        else:
            for i in range(len(level)):
                removed_level = level[:i] + level[i+1:]
                if is_safe(removed_level):
                    counter += 1
                    break
    return counter




def get_answer():
    print(part1(), part2())

if __name__ == "__main__":
    get_answer()
    