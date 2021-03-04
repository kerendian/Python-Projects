'''
return a recursive list as a normal list of numbers by a corect order using recursion
Parameters:
    rec_list(lst) recursive list (a list that contains lists inside lists)
Returns:
    (lst): normal list of numbers by the correct order
'''
def flatten(rec_list):
    if rec_list == []:
        return rec_list
    if isinstance(rec_list[0], list): #method that checks if the object is a list
        return flatten(rec_list[0]) + flatten(rec_list[1:])
    return rec_list[:1] + flatten(rec_list[1:]) #if the first object is not a list
