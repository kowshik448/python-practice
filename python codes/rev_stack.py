from stack import Stack
s=Stack()
string = input()
for i in range(len(string)):
    s.push(string[i])
print(s.get_stack())
rev_string = ''
while not s.is_empty():
    rev_string+=str(s.pop())
rev_stack=Stack()
for i in range(len(string)):
    rev_stack.push(rev_string[i])
print(rev_stack.get_stack())