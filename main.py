from sudoku_board import Board
import time
import turtle

board = Board()
board.fillGrid()
board.remove_number_one_by_one()
board.drawGrid()
board.myPen.getscreen().update()
board.solveSudoku()
board.drawGrid()
board.myPen.getscreen().update()
turtle.mainloop()



