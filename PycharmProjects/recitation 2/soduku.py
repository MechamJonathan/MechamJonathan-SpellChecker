

def main():
    grid = getGrid()
    printGrid(grid)

    if isValid(grid):
        print("valid solution")
    else:
        print("invalid solution")

def printGrid(grid):
    for row in grid:
        for column in row:
            print(column, end = "  ")
        print()

def getGrid():
    grid = []
    file = open("input.txt", "r")
    for i in range(9):
        line = file.readline().split()
        grid.append([eval(char) for char in line])
    return grid

#check if solution is valid
def isValid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] > 9 \
                or not isValidAt(i, j, grid):
                return False
    return True
#check if grid [i][j] is valid in the grid
def isValidAt(i, j, grid):
    for column in range(9):
        if column != j and grid[i][column] == grid[i][j]:
            return False

    for row in range(9):
        if row != i and grid[row][j] == grid[i][j]:
            return False


    for row in range(( i // 3) * 3, (i // 3) * 3 +3):
        for col in range((j // 3) * 3, (j // 3) * 3 + 3):
            if row != i and col != j and \
                grid[row][col] == grid[i][j]:
                return False


    return True



main()