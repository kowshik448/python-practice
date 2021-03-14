arr=[[1,3],[5,8],[4,5],[8,11]]#merge the sub lists
arr.sort()
i=0
c=[]
while i<len(arr)-1:
    a=[]
    if arr[i][1]>=arr[i+1][0]:
        if arr[i][1]>=arr[i+1][1]:
            a=arr[i]
        else:
            a.append(arr[i][0])
            a.append(arr[i+1][1])
        arr[i]=a
        arr.remove(arr[i+1])
        i=i
        if i+1==len(arr):
            c.append(a)
            break
    else:
        a=arr[i]
        c.append(a)
        i+=1
        if i+1==len(arr):
            c.append(arr[-1])
            break
print(c)