# Library containing the methods to push the grid around in 2048 for a 4x4 grid
# Christopher Blignaut 
# BLGCHR003
# 18 April 

def push_up (grid):                             
    """merge grid values upwards"""
    
    # Shifting all values up
    for i in range (1,4):                       
        for j in range(1,4):                    
            for k in range(4):                  
                if grid[j-1][k] == 0:           
                        grid[j-1][k] = grid[j][k]
                        grid[j][k] = 0
                        
    # Checking if any values are combined in this move and combines them                         
    for i in range(3):                          
        for j in range(4):                      
            if grid[i][j] == grid[i+1][j]:      
                    grid[i][j] = grid[i][j] * 2       
                    grid[i+1][j] = 0
                    
    # Shifting all values up after combining certain numbers               
    for i in range(1,4):                        
        for j in range(1,4):                    
            for k in range(4):                  
                if grid[j-1][k] == 0:
                        grid[j-1][k] = grid[j][k]
                        grid[j][k] = 0
                        
                    
    return grid
    
def push_down (grid):                           
    """merge grid values downwards"""
    
    # Shifting all values down
    for n in range (3,0,-1):                    
        for i in range(2,-1,-1):                 
            for j in range(4):                  
                if grid[i+1][j] == 0:
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = 0
                    
    # Checking if any values are combined in this move and combines them                     
    for i in range(2,-1,-1):                     
        for j in range(4):                      
            if grid[i][j] == grid[i+1][j]:
                    grid[i+1][j] = grid[i+1][j] * 2
                    grid[i][j] = 0
                
    # Shifting all values down after combining certain numbers                   
    for n in range(3,0,-1):                      
        for i in range(2,-1,-1):                 
            for j in range(4):                  
                if grid[i+1][j] == 0:
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = 0            
    return grid        
    
def push_left (grid):                           
    """merge grid values left"""
    
    # Shifting all values to the left
    for n in range (1,4):                       
        for i in range(4):                      
            for j in range(1,4):                
                if grid[i][j-1] == 0:
                        grid[i][j-1] = grid[i][j]
                        grid[i][j] = 0
                        
    # Checking if any values are combined in this move and combines them                
    for i in range(4):                           
        for j in range(3):                      
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = grid[i][j] * 2
                grid[i][j+1] = 0
                
    # Shifting all values to the left after combining certain numbers             
    for n in range(1,4):                        
        for i in range(4):                      
            for j in range(1,4):                
                if grid[i][j-1] == 0:
                        grid[i][j-1] = grid[i][j]
                        grid[i][j] = 0            
    return grid

def push_right (grid):                           
    """merge grid values right"""
    
    # Shifting all values to the right
    for i in range (3,0,-1):                    
        for j in range(4):                       
            for k in range(2,-1,-1):             
                if grid[j][k+1] == 0:
                    grid[j][k+1] = grid[j][k]
                    grid[j][k] = 0
    
    # Checking if any values are combined in this move and combines them           
    for i in range(4):                          
        for j in range(2,-1,-1):                 
            if grid[i][j] == grid[i][j+1]:
                    grid[i][j+1] = grid[i][j+1] * 2
                    grid[i][j] = 0
                    
    # Shifting all values to the right after combining certain numbers         
    for i in range(3,0,-1):                     
        for j in range(4):                      
            for k in range(2,-1,-1):             
                if grid[j][k+1] == 0:
                        grid[j][k+1] = grid[j][k]
                        grid[j][k] = 0            
    return grid  
