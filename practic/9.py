import time
import re
from typing import List, Tuple

class HashTable:
    def __init__(self, size=1009, hash_func=None):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.hash_func = hash_func if hash_func else self._good_hash

    def _good_hash(self, key: str) -> int:
        h = 0
        base = 31
        for ch in key:
            h = (h * base + ord(ch)) % self.size
        return h

    def _bad_hash(self, key: str) -> int:
        return 1

    def put(self, key: str, value: int):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str) -> int:
        index = self.hash_func(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return 0  # если не найдено

    def get_all_items(self) -> List[Tuple[str, int]]:
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return items


def preprocess_text(text: str) -> List[str]:
    text = text.lower()
    words = re.findall(r'\b[a-яёa-z]+\b', text)
    return words


def build_frequency_table(words: List[str], use_bad_hash: bool = False) -> HashTable:
    if use_bad_hash:
        ht = HashTable(hash_func=lambda key: 1)
    else:
        ht = HashTable()
    
    for word in words:
        freq = ht.get(word)
        ht.put(word, freq + 1)
    return ht


def get_top10(ht: HashTable) -> List[Tuple[str, int]]:
    items = ht.get_all_items()
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:10]

SAMPLE_TEXT = """
дин два три четыре пять шесть семь восемь девять один один два два
"""

if __name__ == "__main__":

    words = preprocess_text(SAMPLE_TEXT)
    print(f"Обработано {len(words)} слов.\n")

    print("Замер времени с хорошей хэш-функцией")
    start = time.perf_counter()
    ht_good = build_frequency_table(words, use_bad_hash=False)
    time_good = time.perf_counter() - start
    print(f"Время: {time_good:.6f} сек")

    print("\nЗамер времени с плохой хэш-функцией")
    start = time.perf_counter()
    ht_bad = build_frequency_table(words, use_bad_hash=True)
    time_bad = time.perf_counter() - start
    print(f"Время: {time_bad:.6f} сек")

    print(f"\nСравнение:")
    print(f"Хорошая хэш-функция: {time_good:.6f} сек")
    print(f"Плохая хэш-функция:  {time_bad:.6f} сек")
    if time_good > 0:
        print(f"Разница: в {time_bad / time_good:.1f} раз медленнее")

    print("\n10 самых частых слов:")
    top10 = get_top10(ht_good)
    for i, (word, freq) in enumerate(top10, 1):
        print(f"{i:2}. {word:<12} - {freq}")
