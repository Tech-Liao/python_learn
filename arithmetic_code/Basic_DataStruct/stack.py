class stack:
    def __init__(self, size=100):
        self.top = -1
        self.size = size
        self.stack = []

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_fullstack(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def push(self, date):
        if self.is_fullstack():
            print("stack is full")
            return False
        self.stack.append(date)
        self.top += 1
        return True

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return False
        val = self.stack[self.top]
        self.stack.pop()
        self.top -= 1
        return val

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return False
        return self.stack[self.top]

    def print_stack(self):
        if self.is_empty():
            print("stack is empyty")
            return False
        i = self.top
        while i >= 0:
            print(self.stack[i], end=' ')
            i -= 1
        print()
        return True


stack1 = stack()
print(stack1)
stack1.print_stack()
x = [1, 2, 3, 4, 5]

for num in x:
    stack1.push(num)
stack1.print_stack()
stack1.pop()
stack1.print_stack()