import Cell

class SubGrid:
    """
    A class used to represent a SubGrid.
    """
    def __init__(self,i,cells=None):
        """
        Constructor for SubGrid class.
        :param i:  index of the subgrid
        :param cells: list of cell type objects
        """
        self.i = i 
        self.collected_values = []
        if cells is None:
            self.grid = [[0,0,0],[0,0,0],[0,0,0]] 
            for i in range(3): #nested loop, rows and columns
                for j in range(3):
                    self.grid[i][j] = Cell.Cell(i,j)
        else:
            self.grid = [[0,0,0],[0,0,0],[0,0,0]]
            for i in range(3): #nested loop, rows and columns
                for j in range(3):
                    self.grid[i][j] = Cell.Cell(i,j)
            for cell in cells:
                self.grid[cell.i][cell.j] = cell
                self.collected_values.append(cell.values[0])
                
    def update_values(self):
        """
        Method that updates the collected_values list 
        """
        for i in range(3):
            for j in range(3):
                if len(self.grid[i][j].values) == 1 :
                    self.collected_values.append(self.grid[i][j].values[0])
    
    def remove_values(self,cell):
        """
        Method that remove impossible values from values list of each cell
        :param cell: Cell type object
        """
        if len(cell.values) > 1:
            for i in cell.values: #given Cell type value
                if i in self.collected_values:
                    cell.values.remove(i)
        self.update_values() #sograim in method call         
              
    def check_cells_possibilities(self):
        """
        Method that update the values list of each cell
        """
        for i in range(3): #nested loop, rows and columns
            for j in range(3):
                self.remove_values(self.grid[i][j]) #self.grid[i][j] in cell type
                
                
                    
    
                    
                    
                    