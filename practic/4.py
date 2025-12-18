class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_after(self, node, value):
        if node is None:
            raise ValueError("Узел не может быть None")
        new_node = DListNode(value, prev=node, next=node.next)
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        if node == self.tail:
            self.tail = new_node
        if self.head == node and self.tail is None:
            self.tail = node

    def remove_node(self, node):
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def push_back(self, value):
        new_node = DListNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

    def to_list(self):
        return list(self)

if __name__ == "__main__":

    dll = DoublyLinkedList()
    for val in [10, 20, 30]:
        dll.push_back(val)

    print("Исходный список:", dll.to_list())

    current = dll.head
    while current and current.val != 20:
        current = current.next
    node_20 = current

    dll.insert_after(node_20, 25)
    print("После insert_after(20, 25):", dll.to_list())

    dll.remove_node(node_20)
    print("После remove_node(20):", dll.to_list())

    print("Обход через итератор:")
    for val in dll:
        print("  ", val)