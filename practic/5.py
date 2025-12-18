class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class StackArray: #Массив
    def __init__(self):
        self.data = []

    def push(self, x):
        """O(1)"""
        self.data.append(x)

    def pop(self):
        """O(1)"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.data[-1]

class StackList: #Список
    def __init__(self):
        self.head = None

    def push(self, x):
        """O(1) — вставка в голову"""
        new_node = ListNode(x, self.head)
        self.head = new_node

    def pop(self):
        """O(1)"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        val = self.head.val
        self.head = self.head.next
        return val

    def is_empty(self):
        return self.head is None

    def top(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.head.val

def is_valid_parentheses(s: str) -> bool:
    stack = StackArray()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.push(char)
        elif char in pairs:
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

if __name__ == "__main__":

    print("1. Стек на массиве:")
    s1 = StackArray()
    s1.push(10)
    s1.push(20)
    print("  push(10), push(20)")
    print("  pop() =", s1.pop())
    print("  pop() =", s1.pop())
    print("  пуст?", s1.is_empty())

    print("\n2. Стек на связном списке:")
    s2 = StackList()
    s2.push("A")
    s2.push("B")
    print("  push('A'), push('B')")
    print("  pop() =", s2.pop())
    print("  pop() =", s2.pop())
    print("  пуст?", s2.is_empty()) 

    print("\n3. Проверка скобочных последовательностей:")
    test_cases = [
        "()",
        "()[]{}",
        "([{}])",
        "([)]",
        "(((",
        ")))",
        "",
        "{[()]}", 
    ]
    for expr in test_cases:
        result = is_valid_parentheses(expr)
        print(f"  '{expr}' -> {result}")