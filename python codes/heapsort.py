def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l <n and arr[largest]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)

def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for j in range(n-1,0,-1):
        arr[j],arr[0]=arr[0],arr[j]
        heapify(arr,j,0)

arr=[12,11,13,5,6,7]
heapsort(arr)
print(arr)