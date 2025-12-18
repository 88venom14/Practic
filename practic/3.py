import time
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, value):
        new_node = ListNode(value, self.head)
        self.head = new_node

    def pushBack(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def remove(self, value):
        if not self.head:
            return
        if self.head.val == value:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.val != value:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

    def find(self, value):
        cur = self.head
        while cur:
            if cur.val == value:
                return True
            cur = cur.next
        return False

def array_push_front(arr, value):
    arr.insert(0, value)  # O(n)

def array_remove_value(arr, value):
    try:
        arr.remove(value)  # O(n)
    except ValueError:
        pass

def array_find(arr, value):
    return value in arr  # O(n)

def array_push_front(arr, val):
    arr.insert(0, val)  # O(n)

def array_push_back(arr, val):
    arr.append(val)     # O(1)

def array_remove(arr, val):
    try:
        arr.remove(val)  # O(n)
    except ValueError:
        pass

def compare_operations():
    N = 10000
    print(f"равнение операций на {N} элементах\n")

    start = time.perf_counter()
    ll = SinglyLinkedList()
    for i in range(N):
        ll.pushFront(i)
    list_time_front = time.perf_counter() - start

    start = time.perf_counter()
    arr = []
    for i in range(N):
        array_push_front(arr, i)
    array_time_front = time.perf_counter() - start

    print(f"[Вставка в начало]")
    print(f"Список: {list_time_front:.4f} сек")
    print(f"Массив: {array_time_front:.4f} сек")
    print(f"Список быстрее в {array_time_front / list_time_front:.0f} раз\n")

    start = time.perf_counter()
    ll = SinglyLinkedList()
    for i in range(N):
        ll.pushBack(i)
    list_time_back = time.perf_counter() - start

    start = time.perf_counter()
    arr = []
    for i in range(N):
        array_push_back(arr, i)
    array_time_back = time.perf_counter() - start

    print(f"[Вставка в конец]")
    print(f"Список: {list_time_back:.4f} сек")
    print(f"Массив: {array_time_back:.4f} сек")
    print(f"Массив быстрее в {list_time_back / array_time_back:.0f} раз\n")
    ll = SinglyLinkedList()
    for i in range(N):
        ll.pushBack(i)
    arr = list(range(N))
    
    start = time.perf_counter()
    for i in range(0, N, 2):
        ll.remove(i)
    list_time_del = time.perf_counter() - start
    
    start = time.perf_counter()
    for i in range(0, N, 2):
        array_remove(arr, i)
    array_time_del = time.perf_counter() - start

    print(f"[Удаление по значению ({N//2} элементов)]")
    print(f"  Список: {list_time_del:.4f} сек")
    print(f"  Массив: {array_time_del:.4f} сек")
    print(f"Список быстрее в {array_time_del / list_time_del:.1f} раз\n")

if __name__ == "__main__":
    compare_operations()