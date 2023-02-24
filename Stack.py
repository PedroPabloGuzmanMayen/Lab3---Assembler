class Stack: 
    def __init__(self):
        self.modules = []

    def push(self, item):
        self.modules.append(item)

    def pop(self):
        return self.modules.pop()

    def is_empty(self):
        return len(self.modules) == 0

    def peek(self):
        if not self.is_empty():
            return self.modules[-1]

    def size(self):
        return len(self.modules)