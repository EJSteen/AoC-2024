def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    return matrix

def part1():
    matrix = parse_input()
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                counter += get_xmas(matrix, i, j)
    return counter

def part2():
    matrix = parse_input()
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                if (is_x_mas(matrix, i, j)):
                    counter += 1
    return counter
                    
def get_xmas(matrix, row, column):
    counter = 0
    rows, cols = len(matrix), len(matrix[0])
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    conditions = [
        is_valid(row+3, column-3) and matrix[row+1][column-1] == 'M' and matrix[row+2][column-2] == 'A' and matrix[row+3][column-3] == 'S',  # Top-left
        is_valid(row-3, column-3) and matrix[row-1][column-1] == 'M' and matrix[row-2][column-2] == 'A' and matrix[row-3][column-3] == 'S',  # Bottom-left
        is_valid(row+3, column+3) and matrix[row+1][column+1] == 'M' and matrix[row+2][column+2] == 'A' and matrix[row+3][column+3] == 'S',  # Top-right
        is_valid(row-3, column+3) and matrix[row-1][column+1] == 'M' and matrix[row-2][column+2] == 'A' and matrix[row-3][column+3] == 'S',  # Bottom-right
        is_valid(row+3, column) and matrix[row+1][column] == 'M' and matrix[row+2][column] == 'A' and matrix[row+3][column] == 'S',          # Top
        is_valid(row-3, column) and matrix[row-1][column] == 'M' and matrix[row-2][column] == 'A' and matrix[row-3][column] == 'S',          # Bottom
        is_valid(row, column-3) and matrix[row][column-1] == 'M' and matrix[row][column-2] == 'A' and matrix[row][column-3] == 'S',          # Left
        is_valid(row, column+3) and matrix[row][column+1] == 'M' and matrix[row][column+2] == 'A' and matrix[row][column+3] == 'S',          # Right
    ]
    counter += sum(conditions)
    return counter

def is_x_mas(matrix, row, column):
    rows, cols = len(matrix), len(matrix[0])
    letters = []
    
    # Define the positions to check
    positions = [
        (row + 1, column - 1),  # bottom-left
        (row - 1, column - 1),  # top-left
        (row + 1, column + 1),  # bottom-right
        (row - 1, column + 1),  # top-right
    ]
    
    # Check validity of each position before accessing
    for r, c in positions:
        if 0 <= r < rows and 0 <= c < cols and matrix[r][c]:
            letters.append(matrix[r][c])
    
    # Check if there are 2 M's and 2 S's and check if there aren't any 'SAS' or 'MAM'
    return letters.count('M') == 2 and letters.count('S') == 2 and matrix[row-1][column-1] != matrix[row+1][column+1] 


def get_answer():
    print(part1(), part2())

if __name__ == "__main__":
    get_answer()