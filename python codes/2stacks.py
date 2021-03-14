class twostacks():
    def __init__(self,n):
        self.size = n
        self.index1 = -1
        self.index2 = n
        self.arr = [None]*n
    
    def push1(self,x):
        if self.index1<self.index2-1:
            self.arr[self.index1+1]=x
            self.index1+=1
        else:
            print('over flow')
        
    def push2(self,x):
        if self.index1<self.index2-1:
            self.arr[self.index2-1]=x
            self.index2=self.index2-1
        else:
            print('over flow')
    
    def pop1(self):
        if self.index1 >= 0:
            x = self.arr[self.index1]
            self.index1=self.index1-1
            return x
        else:
            print('under flow')
    
    def pop2(self):
        if self.index2 < self.size:
            x = self.arr[self.index2]
            self.index2 = self.index2+1
            return x
        else:
            print('under flow')

s = twostacks(5)
s.push1('a')
s.push1('b')
s.push1('c')
s.push1('1')
s.push1('2')
s.push1('3')
print('poppped element',s.pop1())
print('popped element ',s.pop2())