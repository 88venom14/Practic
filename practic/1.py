class StaticArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0


    def _check_overflow(self):
        if self.size >= self.capacity:
            raise OverflowError("Массив заполнен")


    def _check_index(self, idx, allow_end=False):
        if idx < 0 or idx > self.size if allow_end else idx >= self.size:
            raise IndexError("Неверный индекс")


    def pushBack(self, value):  # O(1)
        self._check_overflow()
        self.data[self.size] = value
        self.size += 1


    def pushFront(self, value):  # O(n)
        self.insert(0, value)


    def insert(self, index, value):  # O(n)
        self._check_index(index, allow_end=True)
        self._check_overflow()
        # Сдвиг вправо
        self.data[index + 1 : self.size + 1] = self.data[index : self.size]
        self.data[index] = value
        self.size += 1


    def remove(self, index):  # O(n)
        self._check_index(index)
        # Сдвиг влево
        self.data[index : self.size - 1] = self.data[index + 1 : self.size]
        self.data[self.size - 1] = None
        self.size -= 1


    def find(self, value):  # O(n)
        try:
            return self.data[:self.size].index(value)
        except ValueError:
            return -1


    def __str__(self):
        return f"[{', '.join(map(str, self.data[:self.size]))}] (размер: {self.size}, ёмкость: {self.capacity})"