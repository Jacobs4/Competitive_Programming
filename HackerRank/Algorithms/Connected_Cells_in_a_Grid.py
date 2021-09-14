# Sheeesh
# In line 9, sum() function takes only 2 arguments, Since we are adding 9 elements, we have to use sum([ elements go here with comma separated ])

def check(grid, i, j):
    
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or str(grid[i][j]) != '1':
        return  0
    
    grid[i][j] = '#'
    
    total =  sum([
        check(grid, i - 1, j - 1), 
        check(grid, i - 1, j    ), 
        check(grid, i - 1, j + 1), 
        check(grid, i    , j - 1), 
        1,                                  
        check(grid, i    , j + 1), 
        check(grid, i + 1, j - 1), 
        check(grid, i + 1, j    ), 
        check(grid, i + 1, j + 1),
    ])
    
    return total


def connectedCell(grid):
    maximum = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if str(grid[i][j]) == '1':
                maximum = max(maximum, check(grid, i, j))
                
    return maximum
