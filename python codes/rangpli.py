def print_rangoli(size):
    # your code goes here
    l1=list(map(chr,range(97,123)))
    m=4*n-3
    for i in range(1,n+1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))
    for i in range(n-1,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(m,'-'))
    
n = int(input())
print_rangoli(n)