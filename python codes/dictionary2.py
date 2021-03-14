n = int(input())
phone_Book={}
for e in range(n):
    x=input().split(' ')
    phone_Book[x[0]]=x[1]
for i in range(n):
    name=input()
    if name in phone_Book:
        print(name+'='+ str(phone_Book[name]))
    else:
        print("Not found")
