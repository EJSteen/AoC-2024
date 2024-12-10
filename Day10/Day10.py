from time import time

def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
        matrix = [[int(x) for x in list(line.strip())] for line in lines]
    return matrix

def part1and2(matrix):
    counter1 = 0
    counter2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                counter1 += walk(matrix, i, j, [])
                counter2 += rate(matrix,i, j, [])
    return counter1, counter2

def part2(matrix):
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                counter += walk(matrix, i, j, [])
    return counter

def rate(matrix, row, col, visited):
    trails = 0
    outgoing = 0
    if matrix[row][col] == 9:
        return 1           
    if row+1 < len(matrix) and matrix[row][col] + 1 == matrix[row+1][col]:
        outgoing += 1
        trails += rate(matrix, row+1, col, visited)
    if row-1 >= 0 and matrix[row][col] + 1 == matrix[row-1][col]:
        outgoing += 1
        trails += rate(matrix, row-1, col, visited)
    if col+1 < len(matrix[0]) and matrix[row][col] + 1 == matrix[row][col+1]:
        outgoing += 1
        trails += rate(matrix, row, col+1, visited)
    if col-1 >= 0 and matrix[row][col] + 1 == matrix[row][col-1]:
        outgoing += 1
        trails += rate(matrix, row, col-1, visited)
    return trails

def walk(matrix, row, col, visited):
    if (row,col) in visited:
        return 0
    visited.append((row, col))
    counter = 0
    if matrix[row][col] == 9:
        return 1           
    if row+1 < len(matrix) and matrix[row][col] + 1 == matrix[row+1][col]:
        counter += walk(matrix, row+1, col, visited)
    if row-1 >= 0 and matrix[row][col] + 1 == matrix[row-1][col]:
        counter += walk(matrix, row-1, col, visited)
    if col+1 < len(matrix[0]) and matrix[row][col] + 1 == matrix[row][col+1]:
        counter += walk(matrix, row, col+1, visited)
    if col-1 >= 0 and matrix[row][col] + 1 == matrix[row][col-1]:
        counter += walk(matrix, row, col-1, visited)
    return counter



def solve():
    puzzle = parse_input()
    print("Part 1 and 2:",part1and2(puzzle))

def get_answer():
    start_time = time()
    solve()
    print("puzzle took", time() - start_time)

if __name__ == "__main__":
    get_answer()