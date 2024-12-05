def parse_input():
    swap = False
    rules = []
    updates = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        if line == "\n":
            swap = True
        elif (swap):
            nums = line.strip().split(',')
            updates.append(nums)
        else:
            nums = line.strip().split('|')
            numTuple = (nums[0], nums[1])
            rules.append(numTuple)
    return rules, updates

def part1():
    rules, updates = parse_input()
    incorrect = []
    counter = 0
    for i in range(len(updates)):
        correct = True
        for j in range(len(updates[i])-1):
            to_check = updates[i][j+1:]
            for k in range(len(to_check)):
                right_order = [True for rule in rules if rule[0] == updates[i][j] and rule[1] == updates[i][j+k+1]]
                if right_order.count(True) == 0:
                    correct = False
        if correct:
            counter += int(updates[i][len(updates[i])//2])
        else:
            incorrect.append(updates[i])
    second = part2(incorrect, rules)
    return counter, second

def part2(incorrect, rules):
    counter = 0
    for list in incorrect:
        for n in range(len(list) - 1, 0, -1):
            swapped = False
            for i in range(n):
                right_order = [True for rule in rules if rule[0] == list[i] and rule[1] == list[i+1]]
                if right_order.count(True) == 0:
                    list[i], list[i+1] = list[i+1], list[i]
                    swapped = True
                if not swapped:
                    continue
        counter += int(list[len(list)//2])
    return counter




def get_answer():
    print(part1())

if __name__ == "__main__":
    get_answer()