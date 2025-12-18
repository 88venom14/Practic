class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть строкой")
        hash_value = 0
        base = 31
        for ch in key:
            hash_value = (hash_value * base + ord(ch)) % self.size
        return hash_value

    def put(self, key: str, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        raise KeyError(f"Ключ '{key}' не найден")

    def remove(self, key: str):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Ключ '{key}' не найден")

    def visualize(self):
        print("\nСостояние хэш-таблицы")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = ', '.join([f"('{k}', {v})" for k, v in bucket])
                print(f"Bucket {i}: [{items}]")
            else:
                print(f"Bucket {i}: [пусто]")

if __name__ == "__main__":
    ht = HashTable(size=7)

    words = [
        ("яблоко", 10),("груша", 5),("апельсин", 8),
        ("манго", 3),
        ("киви", 7),
        ("банан", 12),
        ("ананас", 4)
    ]
    print("Вставка элементов в хэш-таблицу")
    for key, value in words:
        ht.put(key, value)
        print(f"  put('{key}', {value})")

    ht.visualize()

    print(f"Значение для 'банан': {ht.get('банан')}")
    ht.remove("груша")
    print("Удалён ключ 'груша'")

    ht.visualize()