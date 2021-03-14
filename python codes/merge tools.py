def merge_the_tools(string, k):
    n=len(string)
    l=[]
    for i in range(0,n,k):
        l.append(string[i:i+k])
    for j in l:
        output=''
        for k in j:
            if k not in output:
                output+=k
        print(output)
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)