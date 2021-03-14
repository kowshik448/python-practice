'stack reversing using reccursion '
# from stack import Stack2

class Stack():
    def __init__(self):
        self.stack=[]
    def push(self,item):
        return self.stack.append(item)
    def is_empty(self):
        return len(self.stack)==0
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
    def print_stack(self):
        return self.stack

    def insert_at_bottom(self,temp):
        if self.is_empty():
            self.push(temp)
        else:
            item = self.pop()
            self.insert_at_bottom(temp)
            self.push(item)
    
    def reverse_stack(self): 
        if not self.is_empty():
            temp = self.pop()
            self.reverse_stack()
            self.insert_at_bottom(temp)
    
    def sorting_elements(self,temp):
        if  self.is_empty() or temp>self.top():
            self.push(temp)
        else:
            item = self.pop()
            self.sorting_elements(temp)
            self.push(item)
    
    def sort_stack(self):
        if not self.is_empty():
            temp = self.pop()
            self.sort_stack()
            self.sorting_elements(temp)

# "sorting stack using temporory stack"
    def sortstack(self):
        s2=Stack()
        while not s.is_empty():
            temp = s.top()
            s.pop()
            while not s2.is_empty() and int(temp)<int(s2.top()):
                s.push(s2.top())
                s2.pop()
            s2.push(temp)
        print(s2.print_stack())
    
    def get_min(self):
        s2=Stack()
        while not s.is_empty():
            x = s.top()
            s.pop()
            if s2.is_empty():
                s2.push(x)
            elif x>s2.top():
                s2.push(s2.top())
            else:
                s2.push(x)
        return s2.top()
        

        
            
s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(4)
print(s.print_stack(),"\n")
print(s.get_min())
s.push(0)
print(s.get_min())
# s.reverse_stack()
# print(s.print_stack())
# s.insert_at_bottom(5)
# print(s.print_stack())
# s.sortstack()