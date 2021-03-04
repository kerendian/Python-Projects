'''
sums the cost of each step from each floor and taking the minimal
Parameters:
    n(int) number of floors
    taxes(list) list of taxes(int) for each floor
    steps_options(list) list of step_options(int) represents the step that you can take in each floor
Returns:
    the minimal taxes sum(int)  
'''
def minimal_cost_path(n, taxes, steps_options):
    s = -1 
    x = 0
    for i in steps_options: 
        if len(taxes) == 1 :
            return taxes[0]
    
        if i < len(taxes):
            x = taxes[0] + minimal_cost_path(n,taxes[i:],steps_options)   
        if s == -1 :    
            s = x
        else:
            s = min(s,x)
    return s 

'''
memorization by dict for the key:floor and value:the minimum taxes sum
Parameters:
    n(int) number of floors
    taxes(list) list of taxes(int) for each floor
    steps_options(list) list of step_options(int) represents the step that you can take in each floor
    cost_dict(dict) saving inside the dict the floor and minimum taxes sum for memorization
Returns:
     the minimal taxes sum(int)  

'''    
def minimal_cost_path_faster2(n,taxes,steps_options,cost_dict):
    floor = (n+1) - len(taxes)
    if floor in cost_dict:
        return cost_dict[floor] 
    
    s = 0
    x = 0
    for i in steps_options: 
        if len(taxes) == 1 :
            return taxes[0]
        
        if i < len(taxes):
            x = taxes[0] + minimal_cost_path(n,taxes[i:],steps_options)   
        if s == 0 :    
            s = x
        else:
            s = min(s,x)
    cost_dict[floor] = s  #adding a key and its value to the dict
    return s  
    