class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def count_words_with_prefix(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return self._count_words_from(node)

    def _count_words_from(self, node: TrieNode) -> int:
        count = 1 if node.is_end else 0
        for child in node.children.values():
            count += self._count_words_from(child)
        return count

    def delete(self, word: str) -> bool:
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            ch = word[depth]
            if ch not in node.children:
                return False
            should_delete_child = _delete(node.children[ch], word, depth + 1)
            if should_delete_child:
                del node.children[ch]
                return len(node.children) == 0 and not node.is_end
            return False

        return _delete(self.root, word, 0)

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

if __name__ == "__main__":
    trie = Trie()

    words = ["apple", "app", "application", "apply", "appreciate"]
    print("Вставка слов:", words)
    for w in words:
        trie.insert(w)

    test_prefixes = ["app", "appl", "appr", "xyz"]
    print("\nПодсчёт слов по префиксу:")
    for p in test_prefixes:
        cnt = trie.count_words_with_prefix(p)
        print(f"  Префикс '{p}': {cnt} слов")

    print("\nУдаление слова 'app'...")
    deleted = trie.delete("app")
    print(f"  Успешно удалено: {deleted}")
    print(f"  Слово 'app' существует после удаления: {trie.search('app')}")
    print(f"  Слово 'apple' всё ещё существует: {trie.search('apple')}")

    print("\nПосле удаления 'app':")
    for p in ["app", "appl"]:
        cnt = trie.count_words_with_prefix(p)
        print(f"  Префикс '{p}': {cnt} слов")

    print(f"\nУдаление несуществующего слова 'banana': {trie.delete('banana')}")
