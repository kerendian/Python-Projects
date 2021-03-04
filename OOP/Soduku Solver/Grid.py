import SubGrid
import copy

class Grid:
    """
    A class used to represent a Grid.
    """
    def __init__(self,sub_grids=None):
        """
        Constructor for Grid class.
        :param sub_grids:  list of sub grids
        """
        self.rows =[[],[],[],[],[],[],[],[],[]]
        self.columns =[[],[],[],[],[],[],[],[],[]]
        self.sub_grids = [SubGrid.SubGrid(i) for i in range(9)]
        if sub_grids: # like is not None
            for sg in sub_grids:
                self.sub_grids[sg.i] = sg                
       
    def __repr__(self):
        """
        print function override
        """
        res = ''
        for i in range(9):
            if i % 3 == 0:
                res = res + '\n\n'
            for j in range(9):
                if j % 3 == 0:
                    res = res + '    '
                res = res + str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3]) + ' '
            res = res + '\n'
        return res   
    
    def update_values(self):
        """
        Method that updates the rows and columns with the values known for sure
        """
        for sg in self.sub_grids:
           for i in range(3):
               for j in range(3):
                   if len(sg.grid[i][j].values) == 1:
                       if sg.grid[i][j].values[0] not in self.rows[int(sg.i/3)*3+i]:
                           self.rows[int(sg.i/3)*3+i].append(sg.grid[i][j].values[0])
                       if sg.grid[i][j].values[0] not in self.columns[(sg.i%3)*3+j]:
                           self.columns[(sg.i%3)*3+j].append(sg.grid[i][j].values[0])
    
    def remove_values(self,cell,grid_num):
        """
        Method that updates the rows and columns with the values known for sure
        :param cell: specific cell in the grid
        :param grid_num: int - the subgrid number
        """
        if len(cell.values) == 1:
            return 
        cell_copy = copy.deepcopy(cell.values)
        for value in cell_copy:
            if value in self.rows[int(grid_num/3)*3+cell.i]:
               cell.values.remove(value)
            if value in self.columns[(grid_num%3)*3+cell.j]: #same like in update values but with the args in this function
               if value in cell.values: # not removing the same value from column and row 
                   cell.values.remove(value)
           
        self.update_values()
    
    def check_possibilities(self):
        """
        Method that updates the value list of each cell
        """
        for sg in self.sub_grids:
            sg.check_cells_possibilities()
        self.update_values()
        for sg in self.sub_grids:# run  through all cells
           for i in range(3):
               for j in range(3):
                   self.remove_values(sg.grid[i][j],sg.i)
        
        
    
    def is_solved(self):
        """
        Method that cheking if the game finished
        """
        for sg in self.sub_grids:
           for i in range(3):
               for j in range(3):
                    if len(sg.grid[i][j].values) != 1: #HOW to difine this for ALL Cells togather
                         return False  
        return True
      
    def solve(self):
        while not self.is_solved():
            self.check_possibilities()
           
        
    
    
    
