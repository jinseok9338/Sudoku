import turtle
from random import randint, shuffle

class Board:
    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counter = 0

    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.myPen = turtle.Turtle()
        self.myPen.speed(0)
        self.myPen.color("#000000")
        self.myPen.hideturtle()
        self.topLeft_x = -150
        self.topLeft_y = 150


    def __str__(self):
        ceiling = "-------------------------\n"
        line = "|{num1}  {num2}  {num3}|{num4}  {num5}  {num6}|{num7}  {num8}  {num9}|\n"
        lines_list =[]
        for a in (0,3,6):
            for b in (0,3,6):
                lines = line.format(num1 =self.board[a][b] ,num2 =self.board[a][b+1],num3=self.board[a][b+2],num4=self.board[a+1][b],num5=self.board[a+1][b+1],num6=self.board[a+1][b+2],num7=self.board[a+2][b],num8=self.board[a+2][b+1],num9=self.board[a+2][b+2])
                lines_list.append(lines)
        board = ceiling+lines_list[0]+lines_list[1]+lines_list[2]+ceiling+lines_list[3]+lines_list[4]+lines_list[5]+ceiling+lines_list[6]+lines_list[7]+lines_list[8]+ceiling
        return board

    def text(self,message, x, y, size):
        FONT = ('Arial', size, 'normal')
        self.myPen.penup()
        self.myPen.goto(x, y)
        self.myPen.write(message, align="left", font=FONT)

    # A procedure to draw the grid on screen using Python Turtle
    def drawGrid(self):
        intDim = 35
        for row in range(0, 10):
            if (row % 3) == 0:
                self.myPen.pensize(3)
            else:
                self.myPen.pensize(1)
            self.myPen.penup()
            self.myPen.goto(self.topLeft_x, self.topLeft_y - row * intDim)
            self.myPen.pendown()
            self.myPen.goto(self.topLeft_x + 9 * intDim, self.topLeft_y - row * intDim)
        for col in range(0, 10):
            if (col % 3) == 0:
                self.myPen.pensize(3)
            else:
                self.myPen.pensize(1)
            self.myPen.penup()
            self.myPen.goto(self.topLeft_x + col * intDim, self.topLeft_y)
            self.myPen.pendown()
            self.myPen.goto(self.topLeft_x + col * intDim, self.topLeft_y - 9 * intDim)

        for row in range(0, 9):
            for col in range(0, 9):
                if self.board[row][col] != 0:
                    self.text(self.board[row][col], self.topLeft_x + col * intDim + 9, self.topLeft_y - row * intDim - intDim + 8, 18)

    # A function to check if the grid is full
    def checkGrid(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if self.board[row][col] == 0:
                    return False

        # We have a complete grid!
        return True

    def fillGrid(self):
        # Find next empty cell
        for i in range(0, 81):
            row = i // 9 #this method is kind of clever
            col = i % 9
            if self.board[row][col] == 0:
                shuffle(self.numberList)
                for value in self.numberList:
                    # Check that this value has not already be used on this row
                    if not (value in self.board[row]):
                        # Check that this value has not already be used on this column
                        if not value in (self.board[0][col], self.board[1][col], self.board[2][col], self.board[3][col], self.board[4][col], self.board[5][col],self.board[6][col], self.board[7][col], self.board[8][col]):
                            # Identify which of the 9 squares we are working on
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [self.board[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [self.board[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [self.board[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [self.board[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [self.board[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [self.board[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [self.board[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [self.board[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [self.board[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                self.board[row][col] = value
                                if self.checkGrid():
                                    return True
                                else:
                                    if self.fillGrid():
                                        return True
                break
        self.board[row][col] = 0


    # A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solveGrid(self,grid):
        # Find next empty cell
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for value in range(1, 10):
                    # Check that this value has not already be used on this row
                    if not (value in grid[row]):
                        # Check that this value has not already be used on this column
                        if not value in (
                        grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                        grid[6][col], grid[7][col], grid[8][col]):
                            # Identify which of the 9 squares we are working on
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]
                            # Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if self.checkGrid():
                                    self.counter += 1
                                    break
                                else:
                                    if self.solveGrid(self.board):
                                        return True
                break
        grid[row][col] = 0

    def remove_number_one_by_one(self):
        # Start Removing Numbers one by one

        # A higher number of attempts will end up removing more numbers from the grid
        # Potentially resulting in more difficiult grids to solve!
        attempts = 5
        self.counter = 1
        while attempts > 0:
            # Select a random cell that is not already empty
            row = randint(0, 8)
            col = randint(0, 8)
            while self.board[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)
            # Remember its cell value in case we need to put it back
            backup = self.board[row][col]
            self.board[row][col] = 0

            # Take a full copy of the grid
            copyGrid = []
            for r in range(0, 9):
                copyGrid.append([])
                for c in range(0, 9):
                    copyGrid[r].append(self.board[r][c])

            # Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
            self.counter = 0
            self.solveGrid(copyGrid)
            # If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
            if self.counter != 1:
                self.board[row][col] = backup
                # We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
                attempts -= 1

    def findNextCellToFill(self, i, j):
        for x in range(i, 9):
            for y in range(j, 9):
                if self.board[x][y] == 0:
                    return x, y
        for x in range(0, 9):
            for y in range(0, 9):
                if self.board[x][y] == 0:
                    return x, y
        return -1, -1

    def isValid(self, i, j, e):
        rowOk = all([e != self.board[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != self.board[x][j] for x in range(9)])
            if columnOk:
                # finding the top left x,y co-ordinates of the section containing the i,j cell
                secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
                for x in range(secTopX, secTopX + 3):
                    for y in range(secTopY, secTopY + 3):
                        if self.board[x][y] == e:
                            return False
                return True
        return False

    def solveSudoku(self, i=0, j=0):
        i, j = self.findNextCellToFill( i, j)
        if i == -1:
            return True
        for e in range(1, 10):
            if self.isValid(i, j, e):
                self.board[i][j] = e
                if self.solveSudoku( i, j):
                    return True
                # Undo the current cell for backtracking
                self.board[i][j] = 0
        return False



