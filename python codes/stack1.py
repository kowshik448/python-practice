from stack import Stack
# 'converting integer  num to binary'
n = int(input())
def fun(n):
    s=Stack()
    while n>0:
        r = n%2
        s.push(r)
        n=n//2
    bin_num  =''
    while not s.is_empty():
        bin_num +=str(s.pop())
    return bin_num
print(fun(n))
