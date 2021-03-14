n = int(input())
s = set(map(int, input().split()))
m = int(input())
d = {'pop':s.pop,'remove':s.remove,'discard':s.discard}
for i in range(m):
    c=input().split()
    if len(c)>1:
        d[c[0]](int(c[1]))    #   int is req otherwise it will show key error
    else:
        d[c[0]]()
print(s)
print(sum(s))
