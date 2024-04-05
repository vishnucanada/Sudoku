import requests
class Soduko():
    def __init__(self) -> None:
        N = 9
        reponse = requests.get('https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}')
        soduko = reponse.json()['newboard']['grids'][0]['value']

    def printing(self,arr):
        for i in range(N):
            for j in range(N):
                print(arr[i][j], end = " ")
            print()


    def isSafe(grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
    
        for x in range(9):
            if grid[x][col] == num:
                return False
    
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True
    

    def solveSudoku(grid, row, col):
        if (row == N - 1 and col == N):
            return True
        
        if col == N:
            row += 1
            col = 0
    
        if grid[row][col] > 0:
            return self.solveSudoku(grid, row, col + 1)
        
        for num in range(1, N + 1, 1):
            if isSafe(grid, row, col, num):
                grid[row][col] = num
                if solveSudoku(grid, row, col + 1):
                    return True
    
            grid[row][col] = 0
        return False
sample = Soduko()
sample.printing()
printing(soduko)
solveSudoku(soduko,0,0)
printing(soduko)
 