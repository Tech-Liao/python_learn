class Node:

    def __init__(self, date):
        self.value = date
        self.next = None


class Queue:

    def __init__(self):
        head = Node(0)
        self.front = head
        self.rear = head

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def Enqueue(self, date):
        node = Node(date)
        self.rear.next = node
        self.rear = node
        return True

    def Dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return False

        if self.front.next == self.rear:
            node = self.rear
            self.rear = self.front
            return node
        else:
            node = self.front.next
            self.front.next = node.next
            return node

    def front_val(self):
        if self.is_empty():
            print("queue is empty")
            return False

        return self.front.next.value

    def rear_val(self):
        if self.is_empty():
            print("queue is empty")
            return False

        return self.rear.value


q = Queue()
print(q.front.value)
x = [1, 2, 3, 4, 5]
for i in x:
    q.Enqueue(i)

q.Dequeue()
print(q.front_val())
q.Dequeue()
print(q.rear_val())