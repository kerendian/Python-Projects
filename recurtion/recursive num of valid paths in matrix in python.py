'''
cheking if the move in the matrix is valid by difined condisions 
Parameters:
    matrix(list) two dimansional array
    i1(int) index of row1
    j1(int) index of column1
    i2(int) index of row2
    j2(int) index of column2
Returns:
    return True or False
'''
def is_valid_move(matrix, i1, j1, i2, j2):
    if 0 <= i1 < len(matrix) and 0 <= i2 < len(matrix) and len(matrix) > 0 : #why do we need this line?
        if 0 <= j1 < len(matrix[0]) and 0 <= j2 < len(matrix[0]):
            if (i1 == i2+1 and j1 == j2) or (i1 == i2-1 and j1 == j2) or (i1 == i2 and j1 == j2-1) or (i1 == i2 and j1 == j2+1):
                if matrix[i2][j2] > matrix[i1][j1]:
                    return True
          
    return False
'''
wrapper function that calls the recursive function
Parameters:
    matrix(list) two dimansional array
    i2(int) index of row2
    j2(int) index of column2
Returns:
    number(int) of valid ways from one index in the matrix to another
'''
def num_paths(matrix, i2, j2):
    return num_paths2(matrix,0,0,i2,j2)
'''
The recursive function that sums all the valid ways to go from one index in the matrix to another 
Parameters:
    matrix(list) two dimansional array
    i1(int) index of row1
    j1(int) index of column1
    i2(int) index of row2
    j2(int) index of column2
Returns:
    number(int) of valid ways from one index in the matrix to another
'''
def num_paths2(matrix,i1,j1,i2,j2):
    if (i1,j1) == (i2,j2):
        return 1 #sums in every rec call 
        
    s = 0
    
    if is_valid_move(matrix,i1,j1,i1-1,j1):
        s += num_paths2(matrix,i1-1,j1,i2,j2)
    
    if is_valid_move(matrix,i1,j1,i1+1,j1):
        s += num_paths2(matrix,i1+1,j1,i2,j2)    
    
    if is_valid_move(matrix,i1,j1,i1,j1-1):
        s += num_paths2(matrix,i1,j1-1,i2,j2)   
    
    if is_valid_move(matrix,i1,j1,i1,j1+1):
        s += num_paths2(matrix,i1,j1+1,i2,j2)    
        
    return s
