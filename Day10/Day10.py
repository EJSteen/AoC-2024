from time import time

def parse_input():
    with open('test.txt') as f:
        lines = f.readlines()
        matrix = [[int(x) for x in list(line.strip())] for line in lines]
    return matrix

def part1(matrix):
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                counter += walk(matrix, i, j, [])
    return counter



def is_trailhead(matrix, row, col):
    trails = 0
    if row+1 < len(matrix) and matrix[row][col] + 1 == matrix[row+1][col]:
        trails += 1
    if row-1 > 0 and matrix[row][col] + 1 == matrix[row-1][col]:
        trails += 1
    if col+1 < len(matrix[0]) and matrix[row][col] + 1 == matrix[row][col+1]:
        trails += 1
    if col-1 > 0 and matrix[row][col] + 1 == matrix[row][col-1]:
        trails += 1
    if trails > 1:
        return True
    else:
        return False

def walk(matrix, row, col, visited):
    if (row,col) in visited:
        return 0
    visited.append((row, col))
    #print("height: ",matrix[row][col], row, col)
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
    print(puzzle)
    print("Part 1:",part1(puzzle))
    #print("Part 2:",part2(fs))

def get_answer():
    start_time = time()
    solve()
    print("puzzle took", time() - start_time)

if __name__ == "__main__":
    get_answer()