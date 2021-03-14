from array import *
arr=array('i',[])
# n=int(input())
x=list(map(int,input().strip().split()))

for d in x:
    arr.append(d)

arr.reverse()
output=""
for r in arr:
    output+=f"{r}->"    
print(output)