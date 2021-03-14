class Stack2():
    def __init__(self2):
        self2.items = []
    def push(self2,item):
        self2.items.append(item)
    def pop(self2):
        if not self2.is_empty():
            return self2.items.pop()
    def is_empty(self2):
        return self2.items==[]
    def top(self2):
        if not self2.is_empty():
            return self2.items[-1]
    def print_stack(self2):
        return self2.items
