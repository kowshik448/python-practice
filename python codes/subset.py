testcases = int(input())
for i in range(testcases):
    na = int(input())
    a = set(map(int,input().split()))
    nb = int(input())
    b = set(map(int,input().split()))
    if na>nb:
        print('False')
    else:
        print(all(j in b for j in a))
