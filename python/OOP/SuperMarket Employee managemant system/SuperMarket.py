

class SuperMarket:
    """
    A class used to represent a SuperMarket.
    """
    def __init__(self):
        """
        Constructor for SuperMarket class.
        """
        self.employees = {}
        
    def add_employee(self,employee):
        """
        Method that add employee to the existing employees
        :param employee: the employee to add  
        """
        if employee.name in self.employees.keys():
            return False 
        self.employees[employee.name] = employee
        return True
    
    def remove_employee(self,employee_name):
        """
        Method that remove employee from the existing employees
        :param employee_name: the employee to remove  
        """
        if employee_name in self.employees.keys():
            return self.employees.pop(employee_name)
        return None
    
    def add_shift(self,name,shift):
        """
        Method that adding shift to spesific employee by his name
        :param name: str - the employee name 
        :param shift: Shift - the shift we have to add to the employee
        """
        if name in self.employees.keys():
            self.employees[name].add_shift(shift)
            
    def __repr__(self):
        """
        print function override
        """
        if  len(self.employees) == 0:
            return "No Employees found."
        employee_names = []
        for key in self.employees.keys():
            employee_names.append(key) 
        employee_names.sort()    
        employees_dit = ""
        for name in employee_names: 
            employees_dit += str(self.employees[name]) + "\n" 
        employees_dit = employees_dit[:-1]
        return employees_dit 
    


