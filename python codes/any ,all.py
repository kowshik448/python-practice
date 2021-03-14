# n= int(input())
arr = list(map(int,input().split()))
print(all(i>0 for i in arr) and any(str(j)==str(j)[::-1] for j in arr))