class Sudoku_Spot:
  def __init__(self, id, val, row, col, square, verified=False):
    self.id = id
    self.val = val
    self.row = row
    self.col = col
    self.square = square
    self._verified = verified
    self.possible_vals = []

    if self.verified:
      self.possible_vals = [self.val]

  def __str__(self):
    return f"{self.val}" if self.val != '0' else '_'

  def __repr__(self):
    return f"Location: {self.id}, Value: {self.__str__()}, Row: {self.row}, Column: {self.col}, Square: {self.square}, Verified: {self.verified}"

  @property
  def verified(self):
    return self._verified
  
  @verified.setter
  def verified(self, TorF):
    self._verified = TorF
    
