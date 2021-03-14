# n= int(input())
arr = list(map(int,input().split()))
arr.sort()
arr.reverse()
i=0
while arr[i]==arr[i+1]:
    i+=1
else:
    print(arr[i+1])

