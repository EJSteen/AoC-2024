def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    return matrix

def find_guard(matrix):
    guard = {'<', '>', 'v', '^'}
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element in guard:
                return i, j, element
    
    # If no guard is found, raise an error
    raise ValueError("None of the guards ('^', 'v', '<', '>') are in the list")

#def process_step(matrix, index):
    
    
def part1():
    matrix = parse_input()
    index = find_guard(matrix)
    counter = 0
    
    while True:
        index = find_guard(matrix)
        match index[2]:
            case '<':
                is_out_of_bounds = index[1]-1 < 0
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    break
                is_obstacle = matrix[index[0]][index[1]-1] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '^'
                else:
                    matrix[index[0]][index[1]-1] = '<'
                    matrix[index[0]][index[1]] = 'X'
            case '^':
                is_out_of_bounds = index[0]-1 < 0
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    break
                is_obstacle = matrix[index[0]-1][index[1]] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '>'
                else:
                    matrix[index[0]-1][index[1]] = '^'
                    matrix[index[0]][index[1]] = 'X'
            case '>':
                is_out_of_bounds = index[1]+1 >= len(matrix[0])
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    break
                is_obstacle = matrix[index[0]][index[1]+1] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = 'v'
                else:
                    matrix[index[0]][index[1]+1] = '>'
                    matrix[index[0]][index[1]] = 'X'
            case 'v':
                is_out_of_bounds = index[0]+1 >= len(matrix)
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    break
                is_obstacle = matrix[index[0]+1][index[1]] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '<'
                else:
                    matrix[index[0]+1][index[1]] = 'v'
                    matrix[index[0]][index[1]] = 'X'
    for line in matrix:
        counter += line.count('X')
    return counter
        

            

    

def get_answer():
    print(part1())

if __name__ == "__main__":
    get_answer()