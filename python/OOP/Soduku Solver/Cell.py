class Cell:
    """
    A class used to represent a Cell.
    """
    def __init__(self,i,j,value=None):
        """
        Constructor for Cell class.
        :param i: row index in the subgrid
        :param j: column index in the subgrid
        :param values: list of possible values for the cell
        """
        if value is None:
            self.values = [1,2,3,4,5,6,7,8,9]
        else: 
            self.values = [value]
        self.i = i
        self.j = j
    
    def __repr__(self):
        """
        print function override
        """
        if len(self.values) == 1:
            return str(self.values[0])
        return '_'