import copy
from functools import reduce


class Schema:

    def __init__(self, name):
        self.__tables = []
        self.__schema_name = name

    def get_tables(self):
        return self.__tables

    def add_table(self, table):
        self.__tables.append(table)

    def get_name(self):
        return self.__schema_name

    '''
    method find_tables_by_key 
    param self: table object
    param key: str key name
    return: all the Table names in them key represents a key 
    '''
    find_tables_by_key = \
    lambda self,key:list(map(lambda b: b.get_table_name(),\
    list(filter(lambda a: key in a.get_key(),self.get_tables()))))
    #filter return a filtterd list! 

class Table:
    def __init__(self, key_set, other_columns, values_types, table_name):
        self.__key = tuple(key_set)
        self.__other_columns = tuple(other_columns)
        self.__records = []
        self.__table_name = table_name
        self.__values_types = copy.deepcopy(values_types)

    def __repr__(self):
        columns = []
        res = 'Table: '+self.__table_name + '\n'
        res+= "Columns: "
        for key in self.__key:
            res += str(key)+'(Key) '
            columns.append(key)
        for column in self.__other_columns:
            res += column + ' '
            columns.append(column)
        res +='\nRows:\n' 
        for row in self.__records:
            for k in columns:
                res += str(row[k])+'\t'
            res+='\n'
        return res
    
    def add_record(self, row):
        if self.equal_values(row) and self.is_fitted(row) and not self.contains_key(row):
            self.__records.append(row)

    def get_key(self):
        return self.__key
    
    def get_values_types(self):
        return self.__values_types
    
    def get_other_columns(self):
        return self.__other_columns
    
    def get_table_name(self):
        return self.__table_name
    
    def get_records(self):
        return self.__records

    '''
    method columns names 
    param self: table object
    return: a list with all the column names
    '''
    columns_names = lambda self : [x for x in self.get_values_types().keys()]
    '''
    method new_row_keys 
    param self: table object 
    param new_row: dict type, represent a possible recort for adding to the table
    return: the keys from new_row 
    '''
    new_row_keys = lambda self, new_row : [x for x in new_row]
    '''
    method is_fitted
    param self: table object 
    param new_row: dict type, represent a possible recort for adding to the table
    return: True if all the keys in new_row are are fitted the table column names
    and all the table column names are fitted to the keys in new_row.
    otherwise return False
    '''
    is_fitted = lambda self, new_row: \
    all(x in [x for x in new_row] for x in [x for x in self.get_values_types().keys()])\
    and all(x in [x for x in self.get_values_types().keys()] for x in [x for x in new_row]) 
    '''
    method other_record_types 
    param self: table object 
    param new_row: dict type, represent a possible recort for adding to the table
    param a: key from new_row keys list
    return: a dict that map the key with the value type  
    '''
    other_record_types = lambda self, new_row: \
    dict(map(lambda a: (a,type(new_row[a])) ,self.new_row_keys(new_row)))# if i already got the parameters in the outer lambda i dont need them inside!
    #remmember this dict[key] gives the value of the key          
    '''
    method equal_values 
    param self: table object 
    param new_row: dict type, represent a possible recort for adding to the table
    return: return True if all the (key,type(val)) in new_row are in value type in Table 
    and if all the (key,type(val)) in values type are in new_row
    return False if one of the conditions not True
    '''
    equal_values = lambda self, new_row: \
    all(x in self.other_record_types(new_row).items() for x in self.get_values_types().items()) \
    and all(x in self.get_values_types().items() for x in self.other_record_types(new_row).items())
    '''
    method other_row_keys 
    param self: table object 
    param new_row: dict type, represent a possible recort for adding to the table
    param x: represent list of keys from new_row
    return: a dict only with the keys and thier values from new_row
    for returning a dict i used tuple casting on key and value
    '''
    other_row_keys = lambda self, new_row: dict(map(lambda x: (x,new_row[x]),self.get_key()))

    '''
    method contains_key 
    param self: table object 
    param new_row: dict type, represent a possible recort for adding to the table
    param ans: 
    return: return True if all the keys from new_row are already exist in Table False if not 
    '''
    contains_key = lambda self,new_row: any(list(map(lambda ans: self.other_row_keys(new_row) == ans, [self.other_row_keys(x) for x in self.get_records()]))) 
    '''
    method select
    param self: table object 
    param func: given function to filter the records in Table 
    return: a filtered list that filters by given func on all the records in Table 
    '''
    select = lambda self,func : list(filter(func,self.get_records()))
    '''
    method sum_of_column 
    param self: table object 
    param column_name: str represents column name
    param a: represents the values in column name
    return: the sum of the values in column name
    '''
    sum_of_column = \
    lambda self, column_name: \
    reduce(lambda k,z : k+z ,list(map(lambda a: a.get(column_name) ,[x for x in self.get_records()])) , 0)
    # if i use a 3rd param in reduce func it take the 3rd param as a defalt number, if the list is empty it returns 0 

  






    
    
    
    