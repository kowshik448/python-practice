import sys

arr = []
def hgsum(arr,i,j):
    sum=0
    sum+=arr[i-1][j-1]
    sum+=arr[i-1][j]
    sum+=arr[i-1][j+1]
    sum+=arr[i][j]
    sum+=arr[i+1][j-1]
    sum+=arr[i+1][j]
    sum+=arr[i+1][j+1]
    return sum

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_hour_glass_sum=-63
for i in range(1,5):
    for j in range(1,5):
        hour_glass_sum=hgsum(arr,i,j)
        if hour_glass_sum>max_hour_glass_sum:
            max_hour_glass_sum=hour_glass_sum
print(max_hour_glass_sum)


