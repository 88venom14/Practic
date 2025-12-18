import time

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def pushBack(self, value):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1


class StaticArray:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def pushBack(self, value):
        if self.size >= self.capacity:
            raise OverflowError("Массив заполнен")
        self.data[self.size] = value
        self.size += 1


if __name__ == "__main__":
    print("Замер времени вставки 100 000 элементов")

    start = time.time()
    dyn_arr = DynamicArray()
    for i in range(100_000):
        dyn_arr.pushBack(i)
    dyn_time = time.time() - start

    print(f"Динамический массив: {dyn_time:.4f} сек")
    print(f"Размер: {dyn_arr.size}, Емкость: {dyn_arr.capacity}")

    print("\nСтатический массив (ёмкость = 1000)")
    start = time.time()
    try:
        stat_arr = StaticArray(capacity=1000)
        for i in range(100_000):
            stat_arr.pushBack(i)
    except OverflowError:
        stat_time = time.time() - start
        print(f" Переполнение на {i}-м элементе")
        print(f"   Время до ошибки: {stat_time:.4f} сек")