#maximum sum such that no two are adjacent..

arr=[5,  5, 10, 40, 50, 35]
# arr=[1,20,3,4]
def max_sum(arr):
    n=len(arr)
    i=0
    maxxsum1=maxxsum2=0
    maxx=0
    index1=-1
    index2=-1
    while i<n:
        if i==0:
            maxxsum1=arr[0]
            maxx=maxxsum1
            index1=i
            i+=1
        if index1>index2:
            maxxsum2+=arr[i]
            index2=i
            maxx=max(maxxsum1,maxxsum2)
            i+=1
        elif index2>index1:
            maxxsum1+=arr[i]
            index1=i
            maxx=max(maxxsum1,maxxsum2)
            i+=1
    return maxx


def 
            
print(max_sum(arr))