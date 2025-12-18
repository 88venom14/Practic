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

    def _dfs(self, node: TrieNode, prefix: str, results: list):
        if node.is_end:
            results.append(prefix)
        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, results)

    def get_all_words_with_prefix(self, prefix: str) -> list:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._dfs(node, prefix, results)
        return results

class AutocompleteSystem:
    def __init__(self):
        self.trie = Trie()
        self.freq_map = {}

    def add_word(self, word: str):
        word = word.lower()
        self.trie.insert(word)
        self.freq_map[word] = self.freq_map.get(word, 0) + 1

    def autocomplete(self, prefix: str) -> list:
        prefix = prefix.lower()
        candidates = self.trie.get_all_words_with_prefix(prefix)
        candidates.sort(key=lambda w: (-self.freq_map[w], w))
        return candidates

if __name__ == "__main__":
    ac = AutocompleteSystem()
    words = [
        "apple", "application", "apply", "app",
        "banana", "band", "bandana"
    ]
    print("Добавление слов")
    for w in words:
        ac.add_word(w)
        print(f"  + '{w}'")

    print(f"\nЧастоты (HashMap):")
    for word, freq in sorted(ac.freq_map.items()):
        print(f"  {word}: {freq}")


    test_prefixes = ["app", "ban", "a", "x"]

    print("\nАвтодополнение по префиксам:")
    for p in test_prefixes:
        suggestions = ac.autocomplete(p)
        print(f"\nПрефикс: '{p}'")
        if suggestions:
            for i, word in enumerate(suggestions[:5], 1):
                print(f"  {i}. {word} (частота: {ac.freq_map[word]})")
        else:
            print("Нет подсказок")