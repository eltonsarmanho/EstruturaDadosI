class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.capacity = capacity

    def enqueue(self, item):
        if (self.tail + 1) % self.capacity == self.head:
            print("Queue is full")
            return
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self):
        if self.head == self.tail:
            print("Queue is empty")
            return
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        return item


queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3