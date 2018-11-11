import random

# depth-first_search_with_wall_cells

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
        self.is_wall = True
        self.walls = ["N", "S", "E", "W"]
        self.neighbors = ["N", "S", "E", "W"]

def generate_cells(size):
    grid = []
    for i in range(size[0]):
        line = []
        for j in range(size[1]):
            cell = Cell()
            if i%2==0 and j%2==0:
                cell.is_wall = False
            line.append(cell)
        grid.append(line)
    remove_neighbors(grid)
    return grid

def remove_neighbors(grid):
    size = (len(grid), len(grid[0]))
    print(size)
    
    last_size_0 = size[0] if size[0] % 2 != 0 else size[0] - 1
    last_size_1 = size[1] if size[1] % 2 != 0 else size[1] - 1
    print(last_size_0, " - ", last_size_1)
    for i in range(0, last_size_0, 2):
        grid[0][i].neighbors.remove("N")
        grid[last_size_1 - 1][i].neighbors.remove("S")
    for i in range(0, last_size_1, 2):
        grid[i][0].neighbors.remove("W")
        grid[i][last_size_0 - 1].neighbors.remove("E")

def depth_first_search(stack, grid, pos):
    cell = grid[pos[0]][pos[1]]
    cell.visited = True
    random.shuffle(cell.neighbors)
    for i in cell.neighbors:
        move = cell.cell_directions[i]
        next_pos = [pos[0] + move[0], pos[1] + move[1]]
        next_cell = grid[next_pos[0]][next_pos[1]]
        if next_cell.visited == True:
            continue
        else:
            print("pos ", pos, " move ", move, ", next_pos ", next_pos)
            print("i ", i)
            print("neighbors", cell.neighbors)
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
    wall_cell.is_wall = False

def generate_maze(size):
    start = [0, 0]
    grid = generate_cells(size)
    print("cnt - ", len(grid))
    first_cell = grid[start[0]][start[1]]
    maze_stack = [first_cell]

    depth_first_search(maze_stack, grid, start)

    result_grid = []
    for line in grid:
        result_line = []
        for cell in line:
            result_line.append(cell.is_wall)
        result_grid.append(result_line)
    
    return result_grid