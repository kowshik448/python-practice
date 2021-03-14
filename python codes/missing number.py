#missing number for big integers to over come overflow(for python big integer doesnt matter..)
arr=[1,3,4,5,6,7,8,9,10,2,12]
n=len(arr)
total=1
for i in range(2,n+2):
    total+=i
    total-=arr[i-2]
print(total)

#method 2 using xor operator
a=b=0
arr=[3,4,5,6,7,8,9,10,2,12,13,11]
n=len(arr)
for i in range(n):
    a=a^arr[i]
for j in range(1,n+2):
    b=b^j
print(a^b)