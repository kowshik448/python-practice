lst=[1,77,657,1e18]
number_of_elements=len(lst)

# def series(number):
#     if number==0:
#         return 0
#     elif number==1:
#         return 1
#     else:
#         return (9*series(number-1)-4*series(number-2))

def binary_search(element,lower,upper):#lower and upper are indices of array
    middle=(lower+upper)//2
    if lower>upper:
        return False
    if element==series_array[middle]:
        return True
    elif element<series_array[middle]:
        return binary_search(element,lower,middle-1)
    else:
        return binary_search(element,middle+1,upper)

def is_part_of(lst):#lst is a given list of integers
    for element in lst:
        search=binary_search(element,0,len(series_array)-1)
        if (not search):
            return False
    return True

maximum_element=max(lst)
series_array=[0,1]
value=series_array[1]
number=1
while value<=maximum_element:
    number+=1
    # value=series(number)
    value=9*series_array[number-1]-4*series_array[number-2]
    series_array.append(value)
print(is_part_of(lst))
# print(binary_search(77,0,5))