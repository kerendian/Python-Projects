class Clock:
    """
    A class used to represent an Clock.
    """
    def __init__(self,hours,minutes):
        """
        Constructor for Clock class.
        :param hours: int describe the Clock hour
        :param minutes: int describe the Clock minutes
        """
        self.minutes = minutes
        self.hours = hours
        
    def __repr__(self):#represents the way the object will look like when printing 
        """
        print function override
        """
        return (str(self.hours)).zfill(2) + ":" + (str(self.minutes)).zfill(2) #identify if the number is 1 digit ant adds zero befor the number
        #not sure if its ok to usr zfill method

        
    def __add__(self,other):
        """
        addition operator overload
        :param other: a Clock to be added to self
        """
        if isinstance(other,int):
            #other = Clock(other,0)
            hours = self.hours + other
            minutes = self.minutes 
        else:
            hours = self.hours+other.hours 
            minutes = self.minutes+other.minutes 
            if minutes > 59:
                hours += 1
                minutes -= 60 
        return Clock(hours,minutes)
    
    def __radd__(self,other):
        """
        right side addition operator overload
        :param other: a Clock or number to be added with self
        """
        return self + other
            
        
    def __sub__(self,other):
        """
        subtract operator overload
        :param other: a Clock to subtract from self
        """
        hours = self.hours-other.hours 
        minutes = self.minutes-other.minutes
        
        if minutes < 0 : 
            minutes+=60
            hours-=1
            if hours < 0:    
                raise ValueError("Right side clock is greeter than left side")
        if hours < 0 :
            raise ValueError("Right side clock is greeter than left side")
        return Clock(hours, minutes)




