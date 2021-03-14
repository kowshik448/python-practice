def getTotalX(arr, brr):
    lcm = 1
    gcd = brr[0]
    count = 0
    for i in range(n):
        lcm = LCM(lcm,arr[i])
    
    for j in range(1,m):
        gcd = GCD(gcd,brr[j])
    
    if gcd%lcm==0:
        p = int(gcd/lcm)
        for i in  range(1,p+1):
            if gcd%(lcm*i)==0:
                count+=1
    return count
            
def LCM(num1,num2):
    gcd = GCD(num1,num2)
    lcm = num1*num2/gcd   
    return lcm

def GCD(num1,num2):
    if num1>num2:
        num = num1
        den = num2
    else:
        num=num2
        den = num1
    rem = num%den
    while rem!=0:
        num = den
        den = rem
        rem=num%den
    gcd = den
    return gcd

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
