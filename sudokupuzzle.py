# sudokupuzzle.py
#
# Created by:  R. Necaise
# Modified by: Timothy Cohen
#
# Defines an ADT that represents the puzzle grid used with sudoku.
#

from arrays import Array2D

# A sudoku puzzle grid is a 9 x 9 grid that can be used to solve a 
# sudoku puzzle. The grid cells are identified by row and column indices,
# both of which are in the range [0..8] with the upper-left corner
# comprising the first row and first column identified by (0, 0). Each  
# cell of the grid can either be empty, which is indicated with a value 
# of None, or contain a single digit in the range [1..9]. 

class SudokuPuzzleGrid :
   # Creates an empty sudoku puzzle grid.
  def __init__( self ):
    self._grid = Array2D( 9, 9 )
    self._numFilled = 0
    
   # Returns true if all puzzle cells have been filled.
  def isFull( self ):
    return self._numFilled == 81
    
   # Returns true if the given cell is empty, or false otherwise. The 
   # row and column indices must be within the valid range.
  def emptyCell( self, row, col ):
    self._checkRange( row, col )
    return self._grid[row, col] is None
           
   # Returns the value in a given cell or None if the cell is empty. The
   # row and column indices must be within the valid range.
  def getCell( self, row, col ):
    self._checkRange( row, col )
    return self._grid[row,col]
    
   # Sets a cell of the puzzle to a given value. The row and column 
   # indices must be within the valid index range and the value must be
   # within the range [1..9]. 
  def setCell( self, row, col, value ):
    assert value >= 1 and value <= 9, "Value is out of range."
    self._checkRange( row, col )
    self._grid[row, col] = value
    self._numFilled += 1
  
   # Clears the given cell and sets it to be empty. The row and column 
   # indices must be within the valid range.
  def clearCell( self, row, col ):
    self._checkRange( row, col )
    self._grid[row,col] = None
    self._numFilled -= 1
    
   # Clears the entire grid setting all cells to be empty.
  def clearAll( self ):
    self._grid.clear( None )
    self._numFilled = 0
   
   # Determines if setting the puzzle cell, as indicated by the given row
   # and col indices to the given value is a valid sudoku puzzle move.
   # Returns true or false as appropriate. False is also returned if the 
   # given cell indices or value are not valid.
  def validMove( self, row, col, value ):
    if self.isFull():
      return False
    elif row < 0 or row > 8 or col < 0 or col > 8:
      return False#If it's out of range
    else:
      for iterRow in range(0,9):
        if self.getCell(iterRow,col) == value:
          return False #If the value's already in that row
      for iterCol in range(0,9):
        if self.getCell(row,iterCol) == value:
          return False#If the value's already in that col
        
      #To check if it's with the box
    if row < 3:
        if col < 3:
          for iterCol in range(0,3):
            for iterRow in range(0,3):
              if self.getCell(iterRow,iterCol) == value:
                return False
        elif col >= 3 and col < 6:
          for iterCol in range(3,6):
              for iterRow in range(0,3):
                  if self.getCell(iterRow,iterCol) == value:
                      return False          
        else:
          for iterCol in range(6,9):
            for iterRow in range(0,3):
              if self.getCell(iterRow,iterCol) == value:
                return False 
              
    elif row >= 3 and row <6:
      if col < 3:
        for iterCol in range(0,3):
          for iterRow in range(3,6):
            if self.getCell(iterRow,iterCol) == value:
              return False
      elif col >= 3 and col < 6:
        for iterCol in range(3,6):
          for iterRow in range(3,6):
            if self.getCell(iterRow,iterCol) == value:
              return False          
      else:
        for iterCol in range(6,9):
          for iterRow in range(3,6):
            if self.getCell(iterRow,iterCol) == value:
              return False
          
    else:
      if col < 3:
        for iterCol in range(0,3):
          for iterRow in range(6,9):
            if self.getCell(iterRow,iterCol) == value:
              return False
      elif col >= 3 and col < 6:
        for iterCol in range(3,6):
          for iterRow in range(6,9):
            if self.getCell(iterRow,iterCol) == value:
              return False          
      else:
        for iterCol in range(6,9):
          for iterRow in range(6,9):
            if self.getCell(iterRow,iterCol) == value:
              return False       
    
      
    return True#If we've made it this far, it's valid
    
     

   # A helper method that validates row and column indices.
  def _checkRange( self, row, col ):
    assert row >= 0 and row < 9 and col >= 0 and col < 9, \
           "Row or column index out of range."

