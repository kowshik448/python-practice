def array_advance(arr):
    i=0
    further_reached=0
    while i<=further_reached and further_reached<len(arr)-1:
        further_reached=max(further_reached,arr[i]+i)
        i+=1
    if i>further_reached:
        print("unwinnable game")
    else:
        print("we can win!")
    
def array_advance2(arr):
    position=len(arr)-1
    for i in reversed(range(len(arr))):
        if i+arr[i]>=position:
            position =i
    if position==0:
        print("we can win!")
    else:
        print("we lose!!")

arr=[3,3,1,0,2,0,1]
arr2=[5,0,0,0,0,0,0]
array_advance2(arr)