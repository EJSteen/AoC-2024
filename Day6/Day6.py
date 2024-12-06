import copy

def parse_input():
    with open('tests.txt') as f:
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
    
    
def part1():
    matrix = parse_input()
    index = find_guard(matrix)
    counter = 0
    xs = []
    
    while True:
        index = find_guard(matrix)
        match index[2]:
            case '<':
                is_out_of_bounds = index[1]-1 < 0
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
                    break
                is_obstacle = matrix[index[0]][index[1]-1] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '^'
                else:
                    matrix[index[0]][index[1]-1] = '<'
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
            case '^':
                is_out_of_bounds = index[0]-1 < 0
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
                    break
                is_obstacle = matrix[index[0]-1][index[1]] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '>'
                else:
                    matrix[index[0]-1][index[1]] = '^'
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
            case '>':
                is_out_of_bounds = index[1]+1 >= len(matrix[0])
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
                    break
                is_obstacle = matrix[index[0]][index[1]+1] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = 'v'
                else:
                    matrix[index[0]][index[1]+1] = '>'
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
            case 'v':
                is_out_of_bounds = index[0]+1 >= len(matrix)
                if is_out_of_bounds:
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
                    break
                is_obstacle = matrix[index[0]+1][index[1]] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '<'
                else:
                    matrix[index[0]+1][index[1]] = 'v'
                    matrix[index[0]][index[1]] = 'X'
                    xs.append((index[0], index[1]))
    for line in matrix:
        counter += line.count('X')
    return counter, xs
        
def part2():
    amount_xs, xs = part1()
    print(xs)

    matrix = parse_input()
    index = find_guard(matrix)
    counter = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(i, j)
            testmatrix = copy.deepcopy(matrix)
            if not index[0] == i and not index[1] == j:
                testmatrix[i][j] = '#'
            if walk_patrol(testmatrix, index):
                counter += 1
                print(counter)
    return counter
        
def walk_patrol(matrix, index):
    is_visited = {}
    while True:
        index = find_guard(matrix)
        coords = (index[0], index[1])
        print(index, is_visited)
        match index[2]:
            case '<':
                is_out_of_bounds = index[1]-1 < 0
                if is_out_of_bounds:
                    break
                if coords not in is_visited:
                    is_visited[coords] = '<'
                elif is_visited[coords] == '<':
                    return True
                is_visited[coords] = '<'
                is_obstacle = matrix[index[0]][index[1]-1] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '^'
                else:
                    matrix[index[0]][index[1]-1] = '<'
                    matrix[index[0]][index[1]] = '.'
            case '^':
                is_out_of_bounds = index[0]-1 < 0
                if is_out_of_bounds:
                    break
                if coords not in is_visited:
                    is_visited[coords] = '^'
                elif is_visited[coords] == '^':
                    return True
                is_visited[coords] = '^'
                is_obstacle = matrix[index[0]-1][index[1]] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '>'
                else:
                    matrix[index[0]-1][index[1]] = '^'
                    matrix[index[0]][index[1]] = '.'
            case '>':
                is_out_of_bounds = index[1]+1 >= len(matrix[0])
                if is_out_of_bounds:
                    break
                if coords not in is_visited:
                    is_visited[coords] = '>'
                elif is_visited[coords] == '>':
                    return True
                is_visited[coords] = '>'
                is_obstacle = matrix[index[0]][index[1]+1] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = 'v'
                else:
                    matrix[index[0]][index[1]+1] = '>'
                    matrix[index[0]][index[1]] = '.'
            case 'v':
                is_out_of_bounds = index[0]+1 >= len(matrix)
                if is_out_of_bounds:
                    break
                if coords not in is_visited:
                    is_visited[coords] = 'v'
                elif is_visited[coords] == 'v':
                    return True
                is_visited[coords] = 'v'
                is_obstacle = matrix[index[0]+1][index[1]] == '#'
                if is_obstacle:
                    matrix[index[0]][index[1]] = '<'
                else:
                    matrix[index[0]+1][index[1]] = 'v'
                    matrix[index[0]][index[1]] = '.'
    return False
         
    
def get_answer():
    print(part2())

if __name__ == "__main__":
    get_answer()