'''
wrapper function that calls the recursive function 
Parameters:
    lst (list): a list of numbers(int)
Returns:
    True or False
'''
def partition(lst):
    return rec2(lst,0,0)
'''
The recursive function that compair to sums and returns True if they are equal and False if they are not 
Parameters:
    lst(list) list of numbers(int)
    sum1(int) sums the list by recursive calls 
    sum2(int) if sum1 returns false continue to sum2 
Returns:
    True or False
'''
def rec2(lst,sum1,sum2): 
    if len(lst) == 0:
        if sum1 == sum2:
            return True
        return False
    
    if (rec2(lst[1:],sum1+lst[0],sum2)): #first recutsive call, if return false so go on to the second recursive call till the stoping condision 
        return True
    
    if(rec2(lst[1:],sum1,sum2+lst[0])):
        return True
    
    return False