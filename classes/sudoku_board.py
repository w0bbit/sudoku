from .sudoku_spot import Sudoku_Spot

class Sudoku_Board:
  def __init__(self, input):
    self.input = input
    self.board_matrix = []
    
    if len(input) != 81:
      print('INVALID INPUT')
    else:
      id = 0
      for i in range(1,10):
        for j in range(1,10):
          id, val, row, col = id + 1, input[id], i, j
          if row < 4:
            square = 1 if col < 4 else 2 if col < 7 else 3
          elif row < 7:
            square = 4 if col < 4 else 5 if col < 7 else 6
          else:
            square = 7 if col < 4 else 8 if col < 7 else 9
          verified = False if val == '0' else True
          spot = Sudoku_Spot(id, val, row, col, square, verified)
          self.board_matrix.append(spot)

  def display_board(self):
    print('\n')
    display_square = 0
    display_spot = 0
    display_row = []
    display_row_count = 0
    for spot in self.board_matrix:
      display_spot += 1
      display_square += 1
      display_row.append(str(spot))
      if display_spot in (3,6):
        display_row.append('|')
      if display_spot > 8:
        display_row_count += 1
        if display_row_count in (4, 7):
            print('---------------------')
        print(' '.join(display_row))
        display_spot, display_row = 0, []
    print('\n')

  @classmethod
  def id_map(cls):
    print('\n')
    id_square, id_spot, id_row, id_row_count = 0, 0, [], 0
    for num in (n for n in range(1,82)):
      id_spot, id_square = id_spot + 1, id_square + 1
      num = f" {num}" if num < 10 else num
      id_row.append(str(num))
      if id_spot in (3,6):
        id_row.append('|')
      if id_spot > 8:
        id_row_count += 1
        if id_row_count in (4, 7):
            print('------------------------------')
        print(' '.join(id_row))
        id_spot, id_row = 0, []
    print('\n')
          
  def list_row(self, c, v=None):
    c -= 1 #adjustment for diff in index and id
    if v != None:
      return [str(spot) for spot in self.board_matrix if spot.row == self.board_matrix[c].row and spot.verified == v]
    return [str(spot) for spot in self.board_matrix if spot.row == self.board_matrix[c].row]
    
  def list_column(self, c, v=None):
    c -= 1
    if v != None:
      return [str(spot) for spot in self.board_matrix if spot.col == self.board_matrix[c].col and spot.verified == v]
    return [str(spot) for spot in self.board_matrix if spot.col == self.board_matrix[c].col]

  def list_square(self, c, v=None):
    c -= 1
    if v != None:
      return [str(spot) for spot in self.board_matrix if spot.square == self.board_matrix[c].square and spot.verified == v]
    return [str(spot) for spot in self.board_matrix if spot.square == self.board_matrix[c].square]

  def passthrough(self):
    for id in range(1,82):
      spot = self.board_matrix[id-1]
      if len(spot.possible_vals) == 1:
        spot.val = spot.possible_vals[0]
      else:
        possible_nums = []
        if spot.verified == False:
          combined_set = set(self.list_column(id, True) + self.list_row(id, True) + self.list_square(id, True))
          for n in range(1,10):
            if str(n) not in combined_set:
              possible_nums.append(str(n))
        spot.possible_vals = possible_nums
        if len(spot.possible_vals) == 1:
          spot.val = spot.possible_vals[0]
          spot.verified = True

  def solve(self):
    # while not all([spot.verified for spot in self.board_matrix]): #uncomment to keep going until solved
    attempts = (spot for spot in self.board_matrix if not spot.verified)
    for i in attempts:
      self.passthrough()
    if all(spot.verified for spot in self.board_matrix):
      print('SOLVED!')
    else:
      print("STILL UNSOLVED! AND I DON'T KNOW HOW TO GUESS")
    self.display_board()

  
