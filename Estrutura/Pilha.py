class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if self.top == -1:
            return None
        item = self.stack[self.top]
        self.top -= 1
        self.stack.pop()
        return item

    def is_empty(self):
        return self.top == -1

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1