from classes.sudoku_board import Sudoku_Board
from classes.sudoku_spot import Sudoku_Spot
import csv

with open('./sample_sudoku_board_inputs.csv') as csv_file:
  for csv_line in csv.reader(csv_file):
    input = csv_line[0]
    new_board = Sudoku_Board(input)
    print('ORIGINAL BOARD:')
    new_board.display_board()
    print('I GAVE IT MY BEST!')
    new_board.solve()

