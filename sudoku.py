#sudoku.py
#Timothy Cohen

from sudokupuzzle import SudokuPuzzleGrid

def main():
    filename = input("What file do you want to read from?")
    file = open(filename, 'r')
    puzzle = createSudokuPuzzle(file)
    originalPuzzle = puzzle
    found = solveSudokuPuzzle(puzzle,originalPuzzle,0,0)
    printSudokuPuzzle(puzzle)
    
def createSudokuPuzzle(file):
    grid = SudokuPuzzleGrid()
    for line in file:
        line = line.rstrip('\n')
        line = line.split(" ")
        row = int(line[0])
        col = int(line[1])
        value = int(line[2])
        grid.setCell(row,col,value)
    return grid
        

def solveSudokuPuzzle(puzzle,originalPuzzle,row,col):
    if puzzle.isFull():
        return True#End recursion
    if col == 9:#Move down a row
        row += 1
        col = 0   
    if originalPuzzle.getCell(row,col) == None:
        for iterValue in range(1,10):#If it's not an original square
            if puzzle.validMove(row,col,iterValue):
                puzzle.setCell(row,col,iterValue)
                if solveSudokuPuzzle(puzzle,originalPuzzle,row,(col+1)):
                    return True            
                else:
                    puzzle.clearCell(row,col)
    else:#If it's an original square, skip it
        if solveSudokuPuzzle(puzzle,originalPuzzle,row,(col+1)):
            return True
    return False#If we've reached the end

def printSudokuPuzzle(puzzle):
    if puzzle.isFull():#If we've got a valid solution
        print ("Valid Solution")
    else:
        print ("No Valid Solution!")
    for iterRow in range(0,9):
        if iterRow%3 == 0:
            print("  === === ===  === === ===  === === === ")
        else:
            print("  --- --- ---  --- --- ---  --- --- --- ")
        for iterCol in range(0,9):
            value = puzzle.getCell(iterRow,iterCol)
            if value == None:
                value = " "#For invalid solutions
            if iterCol == 0:
                print ("||",value,"| ",end="")
            elif iterCol == 2:
                print (value,end=" || ")
            elif iterCol == 5:
                print (value,end=" || ")                
            elif iterCol == 8:
                print (value,"||")
            else:
                print (value,end=" | ")
    print("  === === ===  === === ===  === === === ")
    
if __name__ == "__main__":#Call the main
    main()

