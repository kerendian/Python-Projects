class Shift:
    """
    A class used to represent a Shift.
    """
    
    def __init__(self,start,finish=None):
        """
        Constructor for Shift class.
        :param start: Clock type describe the begining hour of the shift
        :param finish: Clock type describe the finish hour of the shift
        """
        if finish is None:
            self.duration = start
        else:
            self.duration = finish - start
            
            
    def __repr__(self):
        """
        print function override
        """
        return str(self.duration)
 
    def __add__(self,other):
        """
        addition operator overload
        :param other: a Clock to be added to self
        """
        sum_shifts = self.duration + other.duration
        return Shift(sum_shifts)

