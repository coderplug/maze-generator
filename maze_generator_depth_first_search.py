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
    for i in range(size[0]):
        line = []
        for j in range(size[1]):
            cell = Cell()
            if i%2==1 and j%2==1:
                cell.is_cell = True
            line.append(cell)
        grid.append(line)
    remove_neighbors(grid)
    return grid

def remove_neighbors(grid):
    (max_x, max_y) = (len(grid) - 2, len(grid[0]) - 2)
    (min_x, min_y) = (1, 1)
    print(max_x, " - ", max_y)
    for i in range(min_x, (max_x + 1), 2):
        grid[min_y][i].neighbors.remove("N")
        grid[max_y][i].neighbors.remove("S")
    for i in range(min_y, (max_y + 1), 2):
        grid[i][min_x].neighbors.remove("W")
        grid[i][max_x].neighbors.remove("E")

#TODO: Remake to iterative
def depth_first_search(stack, grid, pos):
    cell = grid[pos[0]][pos[1]]
    cell.visited = True
    random.shuffle(cell.neighbors)
    #while(stack != []):
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
        stack.pop()

def find_wall(grid, pos, direction):
    cell = grid[pos[0]][pos[1]]
    move_wall = cell.wall_directions[direction]
    return grid[pos[0] + move_wall[0]][pos[1] + move_wall[1]]
            
def remove_wall(wall_cell, cell, next_cell, direction):
    cell.walls.remove(direction)
    next_cell.walls.remove(next_cell.dirMirrored[direction])
    wall_cell.is_cell = True

def generate_maze(size):
    start = [1, 1]
    grid = generate_cells(size)
    print("cnt - ", len(grid))
    first_cell = grid[start[0]][start[1]]
    maze_stack = [first_cell]

    depth_first_search(maze_stack, grid, start)

    result_grid = []
    for line in grid:
        result_line = []
        for cell in line:
            result_line.append(cell.is_cell)
        result_grid.append(result_line)
    
    return result_grid