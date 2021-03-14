from collections import deque
stack = deque()
stack.append('a')
stack.appendleft('b')
stack.append('c')



from queue import LifoQueue
stack = LifoQueue(5)
stack.put('a')
stack.put('b')
stack.join()
print(stack.full())
print(stack.get())
print(stack.get())
print(stack.get(timeout=0.5))