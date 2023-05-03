import math
import random

class SudokuGenerator:

  def __init__(self, row_length, removed_cells):
    """This is just the initialzer function in which the variables are assigned"""
    self.row_length = row_length
    self.removed_cells = removed_cells
    self.board = [[0 for i in range(row_length)] for j in range(row_length)]
    self.box_length = int(math.sqrt(row_length))

  def get_board(self): #gets the board so ir can be printed and manipluated
    return self.board

  def print_board(self): #prints the board
    for row in self.board:
      print(row)

  def valid_in_row(self, row, num): #checks if the num is valid in row
    for i in range(self.row_length):
      if self.board[row][i] == num:
        return False
    return True

  def valid_in_col(self, col, num): #Checks if the num is valid in the colum
    for i in range(self.row_length):
      if self.board[i][col] == num:
        return False
    return True

  def valid_in_box(self, row, col, num): #Checks if num is a valid number in place
    row_of_box = row - row % self.box_length
    col_of_box = col - col % self.box_length
    for i in range(row_of_box, row_of_box + self.box_length):
      for j in range(col_of_box, col_of_box + self.box_length):
        if self.board[i][j] == num:
          return False
    return True

  def is_valid(self, row, col, num): #Deterins if a specifc row, box and collum are correct
    if row < 0 or row >= self.row_length or col < 0 or col >= self.row_length:
        return False
    return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)

  def unused_in_box(self, row_start, col_start): #fucntion returns list of unused numbers in a 3x3 box
    used_nums = [
      self.board[row_start + i][col_start + j] for i in range(3)
      for j in range(3)
    ]
    return [i for i in range(1, 10) if i not in used_nums]

  def fill_box(self, row_start, col_start): #Selected unused numbers in empty boxs
    unused_nums = self.unused_in_box(row_start, col_start)
    random.shuffle(unused_nums)
    for i in range(row_start, row_start + 3):
      for j in range(col_start, col_start + 3):
        if self.board[i][j] == 0:
          self.board[i][j] = unused_nums.pop()

  def fill_diagonal(self): #This function fill the diagonal boxes of the grid w random valid numbers
    for i in range(0, self.row_length, 3):
      self.fill_box(i, i)

  def fill_remaining(self, row, col): #this function is used to fill the emppty cells of the grid w valid numbers
    if (col >= self.row_length and row < self.row_length - 1):
      row += 1
      col = 0
    if row >= self.row_length and col >= self.row_length:
      return True #Returns true for the function
    if row < self.box_length:
      if col < self.box_length: #comparing col and box length
        col = self.box_length
    elif row < self.row_length - self.box_length: #comparing row and box legth
      if col == int(row // self.box_length * self.box_length):
        col += self.box_length
    else:
      if col == self.row_length - self.box_length: #Comparing row length and box legth
        row += 1
        col = 0
        if row >= self.row_length:
          return True #Returns true for the function

    for num in range(1, self.row_length + 1):
      if self.is_valid(row, col, num):
        self.board[row][col] = num
        if self.fill_remaining(row, col + 1):
          return True
        self.board[row][col] = 0
    return False

  def fill_values(self):
    """This function fills diagnal boxs in the gride,
    it fill the remaining boxs"""
    self.fill_diagonal()
    self.fill_remaining(0, self.box_length)

  def remove_cells(self):
    """This function removes cells from the board, it has
    a loop that selects a random row and collum using random
    and then sets the value to 0 to remove the cells"""
    cells_to_remove = self.removed_cells
    while cells_to_remove > 0:
      row = random.randint(0, self.row_length - 1)
      col = random.randint(0, self.row_length - 1)
      if self.board[row][col] != 0 and isinstance(self.board[row][col], int):
        self.board[row][col] = 0
        cells_to_remove -= 1


#We did have this as a static method however due to zybooks we had to remove it
def generate_sudoku(size, removed): #this function generates the boarad
  sudoku = SudokuGenerator(size, removed)
  sudoku.fill_values()
  sudoku.remove_cells()
  board = sudoku.get_board()
  return board






