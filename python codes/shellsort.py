def shell_sort(lst):
    gap = len(lst)//2
    while gap>0:
        for index in range(gap,len(lst)):
            curr_val=lst[index]
            pos = index
            while pos>=gap and curr_val<lst[pos-gap]:
                lst[pos]=lst[pos-gap]
                pos-=gap
            lst[pos]=curr_val
        gap=gap//2

lst=[23,34,1,45,67,2]
shell_sort(lst)
print(lst)