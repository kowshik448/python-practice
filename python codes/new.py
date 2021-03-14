t=int(input())
if 1<=t<10:
    for x in range(0,t):
        s=input()
        n=len(s)
        if 2<=n<=10000:
            output=""
            for i in range(0,n,2):
                output+=s[i]
            output+=" "
            for j in range(1,n,2):
                output+=s[j]
            print(output)