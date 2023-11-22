# Module of functions for manipulating a 2D array of size 4x4
# Christopher Blignaut 
# BLGCHR003
# 18 April 

from audioop import reverse
import array


def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    
    # Checking if an empty grid has been entered in as a parameter
    if grid == []:
        for i in range(4):
            miniArr = [0,0,0,0]
            grid.append(miniArr)
        
    else:   
        # initialize values for the array 
        for i in range(4):
            miniArr = []
            for j in range(4):
                miniArr[j] = grid.append(grid)
            grid.append(miniArr)
    
            
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    arr = grid
    out = "|"
    row = ""
    length=0 
    # Organizing the array into a grid 
    for i in range (4):
        col = arr[i]
        for j in range (4):
            row = row+str(col[j])+(" "*(4-(len(str(col[j]))-1))) # Adding the correct amount of spaces for random num generation 
            row = row.replace(",","")
            row = row.replace("[","")
            row = row.replace("]","")
            row = row.replace("0"," ")
        out = out + row +"|\n|"    
        # Determining the number of dashes in the first and last lines which contain plusses
        if len(row)>length:
            if i ==0:
                length = len(row)+1
            else:
                length = len(row)
        row = ""
    
    out = "+"+("-"*(length-1))+"+\n"+out[:len(out)-2]+"\n"+"+"+("-"*(length-1))+"+"
    print (out)

def check_lost (grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""    
    lost = True
    
    # Checking if there are any 0's in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):  
            if grid[i][j]==0:
                lost = False
    
    if lost:
        # Checking if there are any adjacent equal numbers left in the grid       
        for i in range(len(grid)-1):
            for j in range(len(grid[i])-1):            
                if grid[i][j]==grid[i][j+1]:
                    lost = False
                if grid[i][j]==grid[i+1][j]:
                    lost = False
                
    if lost: 
        return True
    else: 
        return False
          
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    
    # Checking if there is a value in the grid that is 32 or larger
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 32:
                won = True          
    return won
def copy_grid (grid):
    """return a copy of the given grid"""
    grid = list(grid)
    copy = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(grid[i][j])
        copy.append(row)
    return copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False  
    