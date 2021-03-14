#2 sorted arrays of equal lengths 
arr1=[1, 12, 15, 26, 38]
arr2=[2, 13, 17, 30, 45]
n=len(arr1)

def merge(arr1,arr2):
    i=j=0
    count=0
    arr=[]
    while count<=n:
        if arr1[i]<=arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
        count+=1
    m=(arr[n]+arr[n-1])//2
    return m

print(merge(arr1,arr2))
