import numpy as np 
import copy 

"""
A class used to represent a MatrixConvolver.
"""    
class MatrixConvolver:
    """
    Constructor for MatrixConvolver class.
    """
    def __init__(self):
        self.matrices_list = []
    
    """
    Method that append matrix to the matrices_list by conditions
    param matrix: given matrix to append to matrices_list
    """       
    def add_matrix(self,matrix):
        if len(self.matrices_list) == 0 : 
            self.matrices_list.append(matrix)
        else:
            if matrix.shape == self.matrices_list[0].shape:
                self.matrices_list.append(matrix)

    """
    Method that remove matrix by conditions on the element. 
    param element: int, ndarray or other to remove from matrices_lis
    """                  
    def remove_matrix(self,element):
        if isinstance(element,(np.ndarray)): #its not good because it can be two same mtrix in the list and we must remove only the first!!  
            for mat in range(len(self.matrices_list)):
                if np.array_equal(self.matrices_list[mat],element):
                    del self.matrices_list[mat] #it was a problem with the remove method and the array_equal... so i used pop
                    break
        elif isinstance(element, int):
            self.matrices_list.pop(element)
        else:
            return -1
    """
    Method that returns a deep copy of matrices_list
    """    
    def get_matrices(self):
        return copy.deepcopy(self.matrices_list)

    
    """
    Method that reshape all matrices in matrices_list to the shape new_shape
    param new_shape: tuple of int numbers that talls the matrix shape by row and column
    """                 
    def reshape_matrices(self,new_shape):
        if len(self.matrices_list) == 0 :
            return 0 

        for i in range(len(self.matrices_list)):
            try:
                self.matrices_list[i] = np.reshape(self.matrices_list[i], new_shape)
                
            except:
                return -1
 
    """
    Method that return the output after performing a convolution.
    param filter_matrix: matrix that performs convolution on one matrix in matrices_list
    param stride_size: int number for stride size
    """                 

    def conv(self,i,filter_matrix, stride_size = 1):
        x,y = filter_matrix.shape
        A,B = self.matrices_list[i].shape
        lst = []
        row = 0
        mat = self.matrices_list[i]
        for k in range(0,A-x+1, stride_size):
            row += 1 
            for i in range(0, B-y+1 , stride_size):
                small_matrix = mat[k:k+x,i:i+y]
                conv = float((np.multiply(filter_matrix,small_matrix)).sum())
                lst.append(conv)
        lst = np.reshape(lst,(row , i+1))     
        return lst




