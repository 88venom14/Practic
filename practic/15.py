class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i: int):
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i: int):
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)

            if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def push(self, val: int):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("Куча пуста")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def build_heap(self, arr: list):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def is_min_heap(self) -> bool:
        n = len(self.heap)
        for i in range(n):
            l, r = self._left(i), self._right(i)
            if l < n and self.heap[i] > self.heap[l]:
                return False
            if r < n and self.heap[i] > self.heap[r]:
                return False
        return True

    def __str__(self):
        return str(self.heap)

if __name__ == "__main__":

    print("1. Вставка и извлечение:")
    h = MinHeap()
    for val in [10, 5, 15, 3, 7]:
        h.push(val)
        is_ok = h.is_min_heap()
        print(f"  push({val}) → {h} (корректность: {is_ok})")

    print("  Извлечение минимума:")
    while h.heap:
        val = h.pop()
        is_ok = h.is_min_heap()
        print(f"    pop() → {val}, остаток: {h} (корректность: {is_ok})")

    print("\n2. Построение кучи из массива:")
    arr = [4, 10, 3, 5, 1]
    h2 = MinHeap()
    h2.build_heap(arr)
    print(f"  Исходный массив: {arr}")
    print(f"  Построенная куча: {h2}")
    print(f"  Корректность: {h2.is_min_heap()}")

    print("\n3. Граничные случаи:")
    h3 = MinHeap()
    h3.build_heap([])
    print(f"Корректность пустой кучи: {h3.is_min_heap()}")

    h4 = MinHeap()
    h4.build_heap([42])
    print(f"Корректность кучи из одного элемента: {h4.is_min_heap()}")