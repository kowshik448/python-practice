from itertools import permutations

word,r=input().split()
for i in list(permutations(sorted(word),int(r))):
    print(''.join(i))
    
