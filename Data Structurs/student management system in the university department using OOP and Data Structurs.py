import copy
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    def __repr__(self):
        return '[' + str(self.value) + ']'


class Tree_node():
    def __init__(self, key, val):
        self.key    = key
        self.val     = val
        self.left    = None
        self.right = None

    def __repr__(self):
         return str(self.key) + ": " + str(self.val)
        
    def is_leaf(self):
        return (self.left == None) and (self.right == None)
    
    def find_successor(self):
        if self.right is None:
            return None
        tmp = self.right
        while tmp.left is not None:
            tmp = tmp.left
        return tmp
        
    
class Binary_search_tree():
    def __init__(self):
        self.root = None

    def search(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)
    
    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val     # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: #key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        
        if self.root == None: #empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)
            
    def find_parent(self,key):
        parent = self.root
        children = self.root
        
        if self.root.key == key:
            return None,self.root
        
        while children.key != key:
            parent = children
            if parent.key > key:
                if parent.left is not None:
                    children = parent.left
                else:
                    return
            elif parent.key < key:
                if parent.right is not None:
                    children = parent.right
                else:
                    return
            else:
                break
        return parent, children

    def delete(self, key):
        if not self.search(key):
            return
        parent, children = self.find_parent(key)
        if children.is_leaf(): # basic case
            if parent is not None:
                if children.key > parent.key:
                    parent.right = None
                else:
                    parent.left = None
                    
            else:
                self.root = None

        elif children.left is None: # has one children - right
            if parent is not None:
                if children.key > parent.key: 
                    parent.right = children.right
                else:
                    parent.left = children.right
            else:
                self.root = children.right
                
        elif children.right is None: # has one children - left
            if parent is not None:
                if children.key < parent.key:
                    parent.left = children.left
                else:
                    parent.right = children.left
            else:
                self.root = children.left
                
        else: # complicate case - 2 children
            successor = children.find_successor()
            successor_parent, successor = self.find_parent(successor.key)
            if successor.right is not None:
                if successor_parent.key != key: # successor_parent shouldn't be deleted
                    successor_parent.left = successor.right
                else:
                    if children.key > parent.key: 
                        parent.right = children.right
                    else:
                        parent.left = children.right
            else: #successor is leaf
                    if successor_parent.key > successor.key:
                        successor_parent.left = None
                    else:
                        successor_parent.right = None
                    children.key = successor.key
                    children.val = successor.val
                        
    def inorder(self):
        ''' return inorder traversal of values as str, uses recursion '''
        def inorder_rec(curr_node , res):
            if curr_node != None:
                inorder_rec(curr_node.left , res)
                res.append((curr_node.key , curr_node.val ))
                inorder_rec(curr_node.right , res)
            return res
            
        if self.root == None: #empty tree
            return []
        else:
            return inorder_rec(self.root, [])
        
            
    def __repr__(self): 
        #no need to understand the implementation of this one
        out = ""
        #need printree.py file or make sure to run it in the NB
        for row in printree(self.root): 
            out = out + row + "\n"
        return out
                
    



def printree(t, bykey = True):
        """Print a textual representation of t
        bykey=True: show keys instead of values"""
        #for row in trepr(t, bykey):
        #        print(row)
        return trepr(t, bykey)

def trepr(t, bykey = False):
        """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
        if t==None:
                return ["#"]

        thistr = str(t.key) if bykey else str(t.val)

        return conc(trepr(t.left,bykey), thistr, trepr(t.right,bykey))

def conc(left,root,right):
        """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""
        
        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)
        
        result = [(lwid+1)*" " + root + (rwid+1)*" "]
        
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid*" " + "\\" + rs*"_" + (rwid-rs)*" ")
        
        for i in range(max(len(left),len(right))):
                row = ""
                if i<len(left):
                        row += left[i]
                else:
                        row += lwid*" "

                row += (rootwid+2)*" "
                
                if i<len(right):
                        row += right[i]
                else:
                        row += rwid*" "
                        
                result.append(row)
                
        return result

def leftspace(row):
        """helper for conc"""
        #row is the first row of a left node
        #returns the index of where the second whitespace starts
        i = len(row)-1
        while row[i]==" ":
                i-=1
        return i+1

def rightspace(row):
        """helper for conc"""
        #row is the first row of a right node
        #returns the index of where the first whitespace ends
        i = 0
        while row[i]==" ":
                i+=1
        return i
class Subject:
    def __init__(self,name,grade,points):
        self.name = name 
        self.grade = float(grade) 
        self.points = float(points)
        
    def __repr__(self):
        return str(self.name) + ", " + str(self.grade)+ "[" + str(self.points)+"]"
    
class Student:
    def __init__(self,name,student_id):
        self.name = name 
        self.student_id = student_id
        self.head = None
        self.points = float(0) 
        
    def add_subjects(self,lst):
        for sub in lst:
            curr = self.head #pointer, to itarate the linked list 
            while curr is not None:
                if curr.value.name == sub.name: # curr is a Node type and his value is subjest, subject is a type and in it we have fields, we go into the name field 
                   
                    if sub.grade >= 56:
                        if curr.value.grade < 56:
                            self.points += sub.points
                    else:
                        if curr.value.grade >=56:
                            self.points -= sub.points                       
                    curr.value = sub
                    break 
                curr = curr.next # continue to the next Node
            if curr is None: #we cheked if sub is not in linked list, and we want to add the sub to the head 
                new_sub = Node(sub)
                new_sub.next = self.head
                self.head = new_sub
                if sub.grade >= 56:
                    self.points += sub.points
                    
    def get_average(self): 
        curr = self.head
        grades_sum = float(0)
        total_points = float(0)
        if curr is None:
            return 0.0
        while curr is not None: #thats how we go over linked list till the None is the end of the list
            grades_sum += curr.value.points* curr.value.grade
            total_points += curr.value.points
            curr = curr.next # to continue the loop on the linked list
        return grades_sum/total_points 
    
    def __eq__(self, other):
        return (self.get_average()) == (other.get_average())
    def __ne__(self, other):
        return (self.get_average()) != (other.get_average())
    def __lt__(self, other):
        return (self.get_average()) < (other.get_average())
    def __le__(self, other):
        return (self.get_average()) <= (other.get_average())
    def __gt__(self, other):
        return (self.get_average()) > (other.get_average())
    def __ge__(self, other):
        return (self.get_average()) >= (other.get_average())
    
    def is_warning(self):
       curr = self.head
       failed_amount = 0
       while curr is not None:
           if curr.value.grade < 56: # add to failed amount only if...
               failed_amount += 1
           if failed_amount >= 2:
               return True 
           curr = curr.next # to iterate on linked list
       if self.get_average() <= 65:
           return True
       else:
           return False

    def __repr__(self):
        curr = self.head 
        if curr is None:
            return "Student " + str(self.name) +"[" +str(self.student_id) + "], avg:0.0, points:0.0, grades:no subjects yet."  
        
        student_print = "Student " + str(self.name) +"[" +str(self.student_id) + "], avg:" + \
            str(self.get_average()) + ", "
        student_print2 = ""
        while curr is not None:
            student_print2 += str(curr.value.name) +"(" + str(curr.value.points) + ")-" +\
            str(curr.value.grade) + ", "
            curr = curr.next
        student_print1 = "points:"+ str(self.points) + ", grades:"   
        student_print+= student_print1 + student_print2
        return student_print[:-2] + "."   
    
    
class ForeignStudent(Student):
    def __init__(self,name,student_id):
        Student.__init__(self,name,student_id) # for inherit from student 
    
    
    def get_average(self): 
        curr = self.head
        grades_sum = 0.0
        total_points = 0.0
        max_grade = []
        if curr is None:
            return 0.0
        while curr is not None: #thats how we go over linked list till the None is the end of the list
            grades_sum += curr.value.points* curr.value.grade
            total_points += curr.value.points
            max_grade.append(curr.value.grade)
            curr = curr.next # to continue the loop on the linked list
        max_grade = max(max_grade)
        return ((grades_sum/total_points) + max_grade)/2
       
   
    def __repr__(self):
        curr = self.head 
        if curr is None:
            return "ForeignStudent " + str(self.name) +"[" +str(self.student_id) + "], avg:0.0, points:0.0, grades:no subjects yet."  
        
        student_print = "ForeignStudent " + str(self.name) +"[" +str(self.student_id) + "], avg:" + \
            str(self.get_average()) + ", "
        student_print2 = ""
        while curr is not None:
            student_print2 += str(curr.value.name) +"(" + str(curr.value.points) + ")-" +\
            str(curr.value.grade) + ", "
            curr = curr.next
        student_print1 = "points:"+ str(self.points) + ", grades:"   
        student_print+= student_print1 + student_print2
        return student_print[:-2] + "."   
    
class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0 
        
    def enqueue(self,val):
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node 
            self.size +=1 
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1 
            
    def dequeue(self):
        if self.head is None:
            return None 
        ans = self.head  
        self.head = self.head.next 
        self.size -=1
        return ans.value

    def front(self):
        if self.head is None:
            return None 
        return self.head.value
    
    def rear(self):
        if self.tail is None:
            return None
        return self.tail.value 
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.head is None #is returns a boolian ans 
    
    def __repr__(self):
        curr = self.head
        queue_lst = [] 
        while curr is not None:
            queue_lst.append(curr.value)          
            curr = curr.next    
        queue_str = ""
        for val in queue_lst:
            queue_str += str(val) + "\n"
        return str(queue_str[:-1]) 
   
class Department():
    def __init__(self,name):
        self.name = name 
        self.students_BST = Binary_search_tree()
        self.id2nodes = {}
        
    def __repr__(self):
        
        student_str = ""
        for val in self.students_BST.inorder():
            student_str += str(val[1]) + "\n"
        return "Department: " + str(self.name) + "\n" + student_str 
    
    def insert(self,student):
        if student.student_id in self.id2nodes:
            return  
        self.students_BST.insert(student.get_average(),student)
        self.id2nodes[student.student_id] = copy.copy(self.students_BST.search(student.get_average()))
 
    def delete_student_by_id(self,student_id):
        if student_id not in self.id2nodes:
            return
        self.students_BST.delete(self.id2nodes[student_id].val.get_average())
        self.id2nodes.pop(student_id)
    
    def add_subject_by_student_id(self,student_id,subject):
        if student_id not in self.id2nodes.keys():
            return 
        my_student = self.id2nodes[student_id]
        self.students_BST.delete(my_student.key)
        sub_lst = [subject]
        my_student.val.add_subjects(sub_lst)
        del self.id2nodes[student_id]
        self.id2nodes[my_student.val.student_id]=  my_student
        self.students_BST.insert(my_student.val.get_average(),my_student.val) 

    def warnings(self):
        warning_student = Queue() #new object Queue type
        students_lst = self.students_BST.inorder() #inorder return sorted list that sorts the tree values by the tree key
        for student in  students_lst:
            if student[1].is_warning():
                warning_student.enqueue(student[1])
        return warning_student
  





