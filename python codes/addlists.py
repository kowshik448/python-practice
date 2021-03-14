lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
def addlists(lst1,lst2):
    arr=[]
    k=min(len(lst1),len(lst2))
    for i in range(k):    
        arr.append(lst1[i]+lst2[i])
    
    if k==len(lst1):
        arr+=lst2[len(lst1):]
    else:
        arr+=lst1[len(lst2):]
    print(arr)

addlists(lst1,lst2)