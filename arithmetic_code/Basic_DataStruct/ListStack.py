class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.Head = None

    def is_empty(self):
        if self.Head is None:
            return True
        else:
            return False

    def push(self, date):
        node = Node(date)
        node.next = self.Head
        self.Head = node

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return False
        node = self.Head
        self.Head = node.next
        return node

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return False
        return self.Head.val

    def print_stack(self):
        if self.is_empty():
            print("stack is empty")
            return False
        cur = self.Head
        while cur is not None:
            print(cur.value, end=' ')
            cur = cur.next
        print()


x = Stack()
print(x)
list1 = [1, 2, 3, 4, 5]
for i in list1:
    x.push(i)
x.print_stack()
node=x.pop()
print(node.value)