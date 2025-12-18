class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            raise OverflowError("Очередь заполнена")
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Очередь пуста")
        val = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return val

    def is_empty(self):
        return self.size == 0

class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def is_empty(self):
        return len(self.data) == 0

class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, x):
        self.in_stack.push(x)

    def dequeue(self):
        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                raise IndexError("Очередь пуста")
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

if __name__ == "__main__":

    print("1. Очередь на циклическом массиве (ёмкость = 5):")
    cq = CircularQueue(capacity=5)
    for i in range(1, 6):
        cq.enqueue(i)
        print(f"  enqueue({i}) → очередь: [{', '.join(str(x) for x in cq.queue)}], head={cq.head}, tail={cq.tail}, size={cq.size}")

    print("  Извлечение элементов:")
    while not cq.is_empty():
        val = cq.dequeue()
        print(f"    dequeue() → {val}, size={cq.size}")

    print("\n2. Очередь на двух стеках:")
    qs = QueueTwoStacks()
    for i in range(10, 16):
        qs.enqueue(i)
        print(f"  enqueue({i})")

    print("  Извлечение элементов:")
    while not qs.is_empty():
        val = qs.dequeue()
        print(f"    dequeue() → {val}")
