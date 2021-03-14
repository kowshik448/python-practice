n = int(input())

def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)

if n < 0:
    print('invalid nmber , please enter positive num ber')
elif n==0:
    print('factoeial of 0 is 1')
else:
    print(recursive_factorial(n))