# s = list(map(str,input().split()))
s = input()
el=[]
ol=[]
ul=[]
ll=[]
for i in s:
    if i.isalpha():
        if i.isupper():
            ul.append(i)
            ul.sort()
        elif i.islower():
            ll.append(i)
            ll.sort()
    elif i.isnumeric():
        if int(i)%2==1:
            ol.append(i)
            ol.sort()
        else:
            el.append(i)
            el.sort()
print(''.join(ll)+''.join(ul)+''.join(ol)+''.join(el))
print("".join(ll+ul+ol+el))