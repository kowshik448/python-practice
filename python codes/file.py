n = int(input())
b = bin(n)
print(b)
x=0
maxx=0
for e in range(len(b)):
    if b[e]=='1':
        x+=1
        if maxx<x:
            maxx=x
    else:
        x=0
print(maxx)

