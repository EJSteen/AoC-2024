from time import time
import itertools

def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    return matrix

def part1(matrix):
    visited = []
    antinodes = []
    do_not_check = ['.', '#']
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not matrix[i][j] in do_not_check and not matrix[i][j] in visited:
                coords = get_same_freq(matrix, matrix[i][j])
                antinodes = get_antinodes(matrix, coords, antinodes)
                visited.append(matrix[i][j])
    return len(antinodes)

def get_same_freq(matrix, antenna):
    coords = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == antenna:
                coords.append((i, j))
    return coords

def get_antinodes(matrix, coords, antinodes):
    counter = 0

    unique_pairs = itertools.combinations(coords, 2)


    for coord1, coord2 in unique_pairs:
        if not coord1 == coord2:
            diff1 = (coord1[0] - coord2[0], coord1[1] - coord2[1])

            diff2 = (coord2[0] - coord1[0], coord2[1] - coord1[1])

            antinode1 = (coord1[0] + diff1[0], coord1[1] + diff1[1])
            if 0 <= antinode1[0] < len(matrix) and 0 <= antinode1[1] < len(matrix[0]) and antinode1 not in antinodes:
                antinodes.append(antinode1)
            
            antinode2 = (coord2[0] + diff2[0], coord2[1] + diff2[1])
            if 0 <= antinode2[0] < len(matrix) and 0 <= antinode2[1] < len(matrix[0]) and antinode2 not in antinodes:
                antinodes.append(antinode2)
    return antinodes


def solve():
    puzzle = parse_input()
    #print(puzzle)
    print(part1(puzzle))
    #print(part2(puzzle))


def get_answer():
    start_time = time()
    solve()
    print("puzzle took", time() - start_time)

if __name__ == "__main__":
    get_answer()