

def parseInput():
    with open('input.txt') as f:
        lines = f.readlines()
    
    leftList = []
    rightList = []
    
    for line in lines:
        nums = line.split('   ')
        left = nums[0].strip()
        right = nums[1].strip()
        leftList.append(left)
        rightList.append(right)
    return leftList, rightList

def part1():
    total = 0
    leftList, rightList = parseInput()
    leftSorted = sorted(leftList)
    rightSorted = sorted(rightList)
    for i in range(len(leftSorted)):
        total += abs(int(leftSorted[i]) - int(rightSorted[i]))
    return total

def part2():
    total = 0
    leftList, rightList = parseInput()
    for i in range(len(leftList)):
        total += int(leftList[i]) * rightList.count(leftList[i])
    return total

def getAnswer():
    print(part1(), part2())

if __name__ == "__main__":
    getAnswer()