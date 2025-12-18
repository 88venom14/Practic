class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)][0] > self.heap[i][0]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)
            if l < n and self.heap[l][0] < self.heap[smallest][0]:
                smallest = l
            if r < n and self.heap[r][0] < self.heap[smallest][0]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def push(self, priority, value):
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Очередь пуста")
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        top_val = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return top_val

    def is_empty(self):
        return len(self.heap) == 0

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def push(self, value, priority):
        self.heap.push(priority, value)

    def pop(self):
        return self.heap.pop()

    def is_empty(self):
        return self.heap.is_empty()

def task_scheduling_demo():
    print("1. Планирование задач:")
    pq = PriorityQueue()
    tasks =[("C", 3),("A", 1),("B", 2),("D", 4)]

    print("  Добавлены задачи:")
    for task, prio in tasks:
        pq.push(task, prio)
        print(f"    '{task}' (приоритет: {prio})")

    print("\n  Порядок выполнения:")
    i = 1
    while not pq.is_empty():
        task = pq.pop()
        print(f"    {i}. {task}")
        i += 1

def k_smallest_elements(arr, k):
    if k <= 0:
        return []
    pq = PriorityQueue()
    for x in arr:
        pq.push(x, x)
    return [pq.pop() for _ in range(min(k, len(arr)))]

def k_smallest_demo():
    print("\n2. Поиск k минимальных элементов:")
    arr = [15, 3, 9, 1, 12, 7, 5]
    k = 4
    print(f"  Массив: {arr}")
    print(f"  k = {k}")
    result = k_smallest_elements(arr, k)
    print(f"  {k} минимальных: {result}")

if __name__ == "__main__":
    task_scheduling_demo()
    k_smallest_demo()