def insertion_sort(lst):
    for index in range(1,len(lst)):
        curr_val=lst[index]
        pos=index
        while curr_val<lst[pos-1] and pos>0:
            lst[pos]=lst[pos-1]
            pos=pos-1
        lst[pos]=curr_val

lst = [5,1,2,4,3,7]
insertion_sort(lst)
print(lst)