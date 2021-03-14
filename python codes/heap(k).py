#first k larger elements

def min_heap(arr,size,k):
    minheap=[]
    for i in range(k):
        minheap.append(arr[i])
    for j in range(k,size):
        minheap.sort()
        if arr[j]>minheap[0]:
            minheap.pop(0)
            minheap.append(arr[j])
        else:
            continue
    print(minheap)

arr=[11, 3, 2, 1, 15, 5, 4,45, 88, 96, 50, 45]
size=len(arr)
k=3
min_heap(arr,size,k)