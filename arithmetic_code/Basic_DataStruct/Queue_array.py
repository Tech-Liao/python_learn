class Queue:
    def __init__(self, size=100):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.front = -1
        self.rear = -1

    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.size - 1:
            return True
        else:
            return False

    def Enqueue(self, date):
        if self.is_full():
            print("queue is full")
            return False
        self.rear += 1
        self.queue[self.rear] = date
        return True

    def Dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return False
        self.front += 1
        val = self.queue[self.front]
        return val

    def peek(self):
        if self.is_empty():
            print("queue is empty")
            return False
        return self.queue[self.front + 1]

    def rear_value(self):
        if self.is_empty():
            print("queue is empty")
            return False
        return self.queue[self.rear]

    def print_queue(self):
        if self.is_empty():
            print("queue is empty")
            return False
        i = self.front + 1
        j = self.rear
        while i <= j:
            print(self.queue[i], end=' ')
            i += 1
        print()


Q = Queue()
print(Q)
x = [1, 2, 3, 4, 5,6,7,8,9]
for i in x:
    Q.Enqueue(i)
value= Q.Dequeue()
Q.print_queue()
v1=Q.peek()
print(v1)
v2 = Q.rear_value()
print(v2)
Q.print_queue()