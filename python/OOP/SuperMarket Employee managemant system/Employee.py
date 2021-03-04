import copy 
import Shift 
import Clock

class Employee:
    """
    A class used to represent an Employee.
    """
    def __init__(self,name):
        """
        Constructor for Employee class.
        :param name: str describe the name of the employee
        """ 
        self.name = name
        self._shifts = []
        
    def __repr__(self):
        """
        print function override
        """
        return "Employee Name: " + self.name + "\n" + "Employee Shifts: " + str(self._shifts)
        
    
    def add_shift(self,shift):
        """
        Method that adding shifts to the list
        :param shift: Shift type object 
        """
        Employee(self._shifts.append(shift))
    
    def get_shifts(self):
        """
        Method that outputs the list of the shifts by deepcopying them
        """
        copy_shifts = copy.deepcopy(self._shifts)
        return copy_shifts  #how to do and use the deep coppy


    
class Manager(Employee):
    """
    A class used to represent a Manager - inherite Employee .
    """
    
    def __init__(self,name,salary):
        """
        Constructor for Manager class.
        :param name: str describe the name of the employee
        :param salary: a number describe the global salary of the manager
        """
        Employee.__init__(self,name)
        self.salary = salary 
        
    def calculate_salary(self):
        """
        Method that calculate the salary of the manager
        """
        manager_shifts = self.get_shifts()
        shifts_time = Shift.Shift(Clock.Clock(0,0)) # must difine a Shift type
        for shift in manager_shifts:
            shifts_time += shift            
        if shifts_time.duration.hours >= 80:
            return self.salary
        else:  #using sum_shifts from the shifts class is ok in this way?
            total_time = shifts_time.duration.hours + (shifts_time.duration.minutes/60)
            salary = int(((total_time/80)*self.salary))
            return salary
    
    def __repr__(self):
        """
        print function override
        """
        manager_print = Employee.__repr__(self)
        manager_print += "\n" +"Salary: " + str(self.calculate_salary()) + "\n" + "Position: Manager" + "\n" + ("="*25)
        return manager_print


class Cashier(Employee):
    """
    A class used to represent a Cashier - inherite Employee .
    """
    def __init__(self,name,salary_per_hour):
        """
        Constructor for Cashier class.
        :param name: str describe the name of the employee
        :param salary_per_hour: a number describe the salary per hour of the cashier
        """
        Employee.__init__(self,name)
        self.salary_per_hour = salary_per_hour
        
    def calculate_salary(self):
        """
        Method that calculate the salary of the cashier
        """
        cashier_shifts = self.get_shifts() 
        shifts_salary = 0        
        for shift in cashier_shifts:
            total_time = shift.duration.hours + (shift.duration.minutes/60) #difining the minutes as a number
            if total_time > 7.5:
                shifts_salary +=(7.5 * self.salary_per_hour)+ (total_time - 7.5)*1.3*self.salary_per_hour
                    
            else:  
                shifts_salary += total_time*self.salary_per_hour
        return int(shifts_salary)
                
    def promote(self,salary):
        """
        Method that promotes the casheir to manager
        """
        m = Manager(self.name,salary) #new object Manager type
        for shift in self.get_shifts():
            m.add_shift(shift)
        return m
              
    def __repr__(self):
        """
        print function override
        """
        cashier_print = Employee.__repr__(self)
        cashier_print += "\n" +"Salary: " + str(self.calculate_salary()) + "\n" + "Position: Cashier" +"\n" + ("="*25)
        return cashier_print  


    
class Stocker(Employee): 
    """
    A class used to represent a Stocker - inherite Employee .
    """
    def __init__(self,name,salary_per_hour):
        """
        Constructor for Stocker class.
        :param name: str describe the name of the employee
        :param salary_per_hour: a number describe the salary per hour of the stocker
        """
        Employee.__init__(self,name)
        self.salary_per_hour = salary_per_hour
        
    def calculate_salary(self):
        """
        Method that calculate the salary of the stocker
        """  
        stocker_shifts = self.get_shifts() 
        shifts_salary = 0        
        for shift in stocker_shifts:
            total_time = shift.duration.hours + (shift.duration.minutes/60) #difining the minutes as a number
            if total_time > 8:
                shifts_salary +=(8 * self.salary_per_hour)+ (total_time - 8)*1.25*self.salary_per_hour
                    
            else:
                shifts_salary += total_time*self.salary_per_hour
        return int(shifts_salary)
        
    def promote(self):        
        """
        Method that promotes the stocker to cashier
        """
        c = Cashier(self.name,self.salary_per_hour + 5) #new object Cashier type
        for shift in self.get_shifts():
            c.add_shift(shift)
        return c
    
    def __repr__(self):
        """
        print function override
        """
        stocker_print = Employee.__repr__(self)
        stocker_print += "\n" +"Salary: " + str(self.calculate_salary()) + "\n" + "Position: Stocker" + "\n" + ("="*25)
        return stocker_print  

