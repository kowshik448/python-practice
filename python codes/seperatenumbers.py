s=input()#seqnce numbers in a string (checking)
n=len(s)

def seperate_numbers(s):
    if n==0:
        return "NO"
    for i in range(1,n//2+1):
        sub_string=s[:i]
        if sqnc(s,sub_string):
            return "YES "+sub_string
    return "NO"

def sqnc(s,sub_string):
    if len(s)==0:
        return True
    elif s.startswith(sub_string):
        l=len(sub_string)
        sub_string=str(int(sub_string)+1)
        s=s[l:]
        return sqnc(s,sub_string)
    else:
        return False        

print(seperate_numbers(s))