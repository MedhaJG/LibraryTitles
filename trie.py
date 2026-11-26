class TrieNode:
    def __init__(self):
        self.children = {}
        self.ids = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, record_id):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.ids.add(record_id)

    def search(self, pattern):
        node = self.root

        for ch in pattern:
            if ch not in node.children:
                return set()

            node = node.children[ch]

        return node.ids