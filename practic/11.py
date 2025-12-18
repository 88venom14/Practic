class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def find(self, val):
        return self._find(self.root, val)

    def _find(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._find(node.left, val)
        else:
            return self._find(node.right, val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_val = self._min_value(node.right)
            node.val = min_val
            node.right = self._delete(node.right, min_val)
        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node.val

    def inorder(self):
        return self._traverse(self.root, "in")

    def preorder(self):
        return self._traverse(self.root, "pre")

    def postorder(self):
        return self._traverse(self.root, "post")

    def _traverse(self, node, order):
        if not node:
            return []
        res = []
        if order == "pre":
            res.append(node.val)
        res += self._traverse(node.left, order)
        if order == "in":
            res.append(node.val)
        res += self._traverse(node.right, order)
        if order == "post":
            res.append(node.val)
        return res

    def is_balanced(self):
        def height(node):
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1 
            return max(left_h, right_h) + 1
        return height(self.root) != -1

if __name__ == "__main__":

    bst = BST()

    values = [10, 5, 15, 3, 7]
    print("Вставка значений:", values)
    for v in values:
        bst.insert(v)

    print("\nПоиск:")
    for v in [7, 20]:
        print(f"  find({v}) = {bst.find(v)}")

    print("\nОбходы:")
    print("  in-order   :", bst.inorder())
    print("  pre-order  :", bst.preorder())
    print("  post-order :", bst.postorder())

    print("\nУдаление значения 10")
    bst.delete(10)
    print("  in-order после удаления:", bst.inorder())


    print("\nПроверка баланса")
    bst_degenerate = BST()
    for val in [1, 2, 3, 4, 5]:
        bst_degenerate.insert(val)
        print(" Вырожденное дерево [1,2,3,4,5]", bst_degenerate.is_balanced())
        print("  После операций:", bst.is_balanced())
