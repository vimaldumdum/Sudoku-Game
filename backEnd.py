grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def findMissing(grid):
    miss = list()

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                miss.append([i, j])

    if len(miss) > 0:
        return miss
    return None


def isSafeBox(rowStart, colStart, grid, key):
    for row in range(3):
        for col in range(3):
            if grid[row + rowStart][col + colStart] == key:
                return False

    return True


def isSafe(row, col, grid, key):
    for i in range(9):
        if grid[row][i] == key and i != col:
            return False

    for i in range(9):
        if grid[i][col] == key and i != row:
            return False

    if isSafeBox(row - row % 3, col - col % 3, grid, key) == False:
        return False

    return True


val = list()


def fillMissing(grid, miss, i):
    if i < len(miss) - 1:
        row = miss[i][0]
        col = miss[i][1]
        for key in range(1, 10):
            if isSafe(row, col, grid, key) == True:
                grid[row][col] = key
                if fillMissing(grid, miss, i + 1) == True:
                    val.append(key)
                    return True
                else:
                    grid[row][col] = 0

    if i == len(miss) - 1:
        row = miss[i][0]
        col = miss[i][1]
        for key in range(1, 10):
            if isSafe(row, col, grid, key) == True:
                val.append(key)
                return True


def solve(grid):
    missing = findMissing(grid)
    # print(missing)

    if not missing:
        return True

    if fillMissing(grid, missing, 0) == True:
        print("Solution exists")
        val.reverse()

        for i in range(len(missing)):
            row = missing[i][0]
            col = missing[i][1]

            grid[row][col] = val[i]
        return True
    else:
        print("Solution does not exists")
        return False


def printGrid(grid):
    for gr in grid:
        print(gr)

def getGrid():
    return grid

