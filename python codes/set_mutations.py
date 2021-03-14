# na = int(input())
a = set(map(int,input().split()))
d={'update':a.update,'intersection_update':a.intersection_update,'symmetric_difference_update':a.symmetric_difference_update,'difference_update':a.difference_update}
for i in range(int(input())):
    c = input().split()
    b = set(map(int,input().split()))
    d[c[0]](b)
print(a)
print(sum(a))