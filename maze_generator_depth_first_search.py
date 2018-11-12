import random

# depth-first_search_with_wall_cells
#TODO: fix recursion limit

class Cell(object):
    def __init__(self):
        self.cell_directions = {
            "N" : [-2, 0],
            "S" : [2, 0],
            "E" : [0, 2],
            "W" : [0, -2]}
        self.wall_directions = {
            "N" : [-1, 0],
            "S" : [1, 0],
            "E" : [0, 1],
            "W" : [0, -1]}
        self.dirMirrored = {
            "N" : "S",
            "S" : "N",
            "E" : "W",
            "W" : "E"}
        self.visited = False
        self.is_cell = False
        self.walls = ["N", "S", "E", "W"]
        self.neighbors = ["N", "S", "E", "W"]

def generate_cells(size):
    grid = []
    (size_row, size_col) = size
    print("size is ", size)
    for i in range(size_row):
        line = []
        for j in range(size_col):
            cell = Cell()
            if i%2==1 and j%2==1:
                cell.is_cell = True
            line.append(cell)
        grid.append(line)
    remove_neighbors(grid)
    return grid

def remove_neighbors(grid):
    (min_row, min_col) = (1, 1)
    (count_row, count_col) = (len(grid), len(grid[0]))
    (max_row, max_col) = (count_row - 2, count_col - 2)
    
    print(max_row, " - ", max_col)
    for i in range(min_row, (max_row + 1), 2):
        print("(i, min_col, max_col) - ", (i, min_col, max_col))
        grid[i][min_col].neighbors.remove("W")
        grid[i][max_col].neighbors.remove("E")
    for i in range(min_col, (max_col + 1), 2):
        print("(i, min_row, max_row) - ", (i, min_row, max_row))
        grid[min_row][i].neighbors.remove("N")
        grid[max_row][i].neighbors.remove("S")

def depth_first_search(grid, pos):
    pos_stack = [pos]
    (pos_row, pos_col) = pos
    stack = [grid[pos_row][pos_col]]
    while(stack != []):
        (pos_row, pos_col) = pos_stack[-1]
        pos = (pos_row, pos_col)
        cell = stack[-1]
        cell.visited = True
        random.shuffle(cell.neighbors)
        back = True
        for neighbor in cell.neighbors:
            #print("(pos, neighbor) - ", (pos_stack[-1], neighbor))
            move = cell.cell_directions[neighbor]
            (move_row, move_col) = move
            next_pos = [pos_row + move_row, pos_col + move_col]
            (next_pos_row, next_pos_col) = next_pos
            next_cell = grid[next_pos_row][next_pos_col]
            if next_cell.visited == True:
                continue
            else:
                """ print("pos ", pos, " move ", move, ", next_pos ", next_pos)
                print("neighbor ", neighbor)
                print("neighbors", cell.neighbors) """
                wall = find_wall(grid, pos, neighbor)
                remove_wall(wall, cell, next_cell, neighbor)
                stack.append(next_cell)
                pos_stack.append(next_pos)
                back = False
                break
        if back is True:
            stack.pop()
            pos_stack.pop()

#TODO: Remake to iterative
""" def depth_first_search(stack, grid, pos):
    cell = stack.
    cell.visited = True
    random.shuffle(cell.neighbors)
    while(stack != []):
    for i in cell.neighbors:
        move = cell.cell_directions[i]
        next_pos = [pos[0] + move[0], pos[1] + move[1]]
        next_cell = grid[next_pos[0]][next_pos[1]]
        if next_cell.visited == True:
            continue
        else:
            #print("pos ", pos, " move ", move, ", next_pos ", next_pos)
            #print("i ", i)
            #print("neighbors", cell.neighbors)
            wall = find_wall(grid, pos, i)
            remove_wall(wall, cell, next_cell, i)
            stack.append(next_cell)
            depth_first_search(stack, grid, next_pos)
        stack.pop() """

def find_wall(grid, pos, direction):
    (pos_row, pos_col) = pos
    cell = grid[pos_row][pos_col]
    (move_row, move_col) = cell.wall_directions[direction]
    return grid[pos_row + move_row][pos_col + move_col]
            
def remove_wall(wall_cell, cell, next_cell, direction):
    cell.walls.remove(direction)
    next_cell.walls.remove(next_cell.dirMirrored[direction])
    wall_cell.is_cell = True

def generate_maze(size):
    (first_row, first_col) = [1, 1]
    grid = generate_cells(size)

    start = (first_row, first_col)

    depth_first_search(grid, start)

    result_grid = []
    for line in grid:
        result_line = []
        for cell in line:
            result_line.append(cell.is_cell)
        result_grid.append(result_line)
    print(result_grid)
    return result_grid