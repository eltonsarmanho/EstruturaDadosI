class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.top += 1
        self.stack.insert(self.top,item)
    def stack_empty(self):
        if self.top == -1:
            return True;
        else:
            return False;
    def pop(self):
        if self.stack_empty():
            return None
        item = self.stack[self.top]
        self.top -= 1
        self.stack.pop()
        return item

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 1
    stack.push(10)
    print(stack.pop())  # Output: 10
