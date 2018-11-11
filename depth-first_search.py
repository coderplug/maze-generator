import random

class Cell(object):
    def __init__(self):
        self.directions = {
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
        self.walls = ["N", "S", "E", "W"]
        self.neighbors = ["N", "S", "E", "W"]

def generate_cells(size):
    grid = []
    for i in range(size[0]):
        line = []
        for j in range(size[1]):
            line.append(Cell())
        grid.append(line)
    remove_neighbors(grid)
    return grid

def remove_neighbors(grid):
    size = (len(grid), len(grid[0]))
    print(size)
    for i in range(size[0]):
        grid[0][i].neighbors.remove("N")
        grid[size[1]-1][i].neighbors.remove("S")
    for i in range(size[1]):
        grid[i][0].neighbors.remove("W")
        grid[i][size[0]-1].neighbors.remove("E")

def depth_first_search(stack, grid, cell, pos):
    cell.visited = True
    random.shuffle(cell.neighbors)
    for i in cell.neighbors:
        move = cell.directions[i]
        next_pos = [pos[0] + move[0], pos[1] + move[1]]
        next_cell = grid[next_pos[0]][next_pos[1]]
        if next_cell.visited == True:
            continue
        else:
            print("pos ", pos, " move ", move, ", next_pos ", next_pos)
            print("i ", i)
            print("neighbors", cell.neighbors)
            cell.walls.remove(i)
            next_cell.walls.remove(next_cell.dirMirrored[i])
            stack.append(next_cell)
            depth_first_search(stack, grid, next_cell, next_pos)
    stack.pop()
    
size = (6, 6)
grid = generate_cells(size)
start = [0, 0]
first_cell = grid[start[0]][start[1]]
maze_stack = [first_cell]

for line in grid:
    for cell in line:
        print(cell.walls)
    print()

depth_first_search(maze_stack, grid, first_cell, start)

for line in grid:
    for cell in line:
        print(cell.walls)
    print()
