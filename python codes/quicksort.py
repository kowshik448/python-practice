def pivot_index(lst,first,last):
    pivot=lst[first]
    left=first+1
    right = last
    while left<=right:
        while left<=right and lst[left]<=pivot:
            left+=1
        while left<=right and lst[right]>=pivot:
            right-=1
        if left<=right:
            lst[left],lst[right]=lst[right],lst[left]
    if left>right:
        lst[first],lst[right]=lst[right],lst[first]
    return right

def quicksort(lst,first,last):
    if first<last:
        p=pivot_index(lst,first,last)
        quicksort(lst,first,p-1)
        quicksort(lst,p+1,last)

lst=[2,5,1,34,0,45,56]
quicksort(lst,0,len(lst)-1)
print(lst)