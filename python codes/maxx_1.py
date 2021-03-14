arr=[]
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    arr.append([name,score])
arr.sort()
maxx1=0
maxx2=0
for i in range(n):
    if maxx1<=arr[i][1]:
        maxx1 = arr[i][1]
for j in range(n):
    if maxx2<arr[j][1]<maxx1:
        maxx2 = arr[j][1]
for l in arr:
    for k in l:
        if k==maxx2:
            print(l[0])
print(arr)