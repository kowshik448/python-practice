n = int(input())
def reccursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return reccursive_fibonacci(n-1) + reccursive_fibonacci(n-2)


if n<=0:
    print('invalid input,please enter positive number')
else:
    for i in range(n):
        print(reccursive_fibonacci(i))