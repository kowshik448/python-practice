from  stack2 import Stack2
s = Stack2()
string = input()
is_balanced = True

def is_match(a,b):
    if a=='(' and b==')':
        return True
    elif a=='['and b==']':
        return True
    elif a=='{' and b=='}':
        return True


for i in string:
    if i in '({[':
        s.push(i)
    else:
        if s.is_empty():
            is_balanced=False
            break
        else:
            top = s.pop()
            if not is_match(top,i):
                is_balanced=False
                break
                

if s.is_empty() and is_balanced:
    print('balanced')
else:
    print('not balanced')