#median of 2 sorted arrays of equal length
arr1=[1, 2, 3, 6]
arr2=[6, 7, 8, 10]

def median(arr1,arr2):
    n=len(arr1)
    if n==1:
        return (arr1[0]+arr2[0])//2
    if n==2:
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))//2
    if n%2==0:
        m1=(arr1[n//2]+arr1[n//2-1])//2
        m2=(arr2[n//2]+arr2[n//2-1])//2
    else:
        m1=arr1[n//2]
        m2=arr2[n//2]
    if m1<m2:
        if n%2==0:
            return median(arr1[n//2-1:],arr2[:n//2+1])
        else:
            return median(arr1[n//2:],arr2[:arr2[n//2+1]])
    else:
        if n%2==0:
            return median(arr1[:n//2+1],arr2[n//2-1:])
        else:
            return median(arr1[:n//2+1],arr2[n//2:])

print(median(arr1,arr2))
