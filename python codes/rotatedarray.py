arr=[3,4,5,6,1,2]
key=6

def search(arr,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==key:
        return mid
    if arr[mid]>=arr[low]:
        if arr[mid]>key and key>=arr[low]:
            return search(arr,low,mid-1,key)
        return search(arr,mid+1,high,key)
    if arr[high]>=key and arr[mid]<=key:
        return search(arr,mid+1,high,key)
    return search(arr,low,mid-1,key)

    
print(search(arr,0,5,key))