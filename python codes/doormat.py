s='.|.'
n,m =map(int,input().split())#m=3n
for i in range(1,n,2):
    print((s*i).center(m,'-'))
print(('welcome').center(m,'-'))
for j in reversed(range(1,n,2)):
    print((s*j).center(m,'-'))

