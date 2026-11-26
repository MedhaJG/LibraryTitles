from trie import Trie
from record import Record


class SearchIndex:

    def __init__(self):
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        self.records = {}

    def build_index(self, catalog):

        for idx, word in enumerate(catalog):

            self.records[idx] = Record(idx, word)

            self.prefix_trie.insert(word, idx)

            reversed_word = word[::-1]
            self.suffix_trie.insert(reversed_word, idx)

    def search(self, prefix, suffix):

        prefix_matches = self.prefix_trie.search(prefix)

        suffix_matches = self.suffix_trie.search(
            suffix[::-1]
        )

        common_ids = prefix_matches & suffix_matches

        if not common_ids:
            return None

        latest_id = max(common_ids)

        return self.records[latest_id]

    def search_with_stats(self, prefix, suffix):

        prefix_matches = self.prefix_trie.search(prefix)

        suffix_matches = self.suffix_trie.search(
            suffix[::-1]
        )

        common_ids = prefix_matches & suffix_matches

        print("\n----- SEARCH STATISTICS -----")
        print("Prefix Candidates :", len(prefix_matches))
        print("Suffix Candidates :", len(suffix_matches))
        print("Intersection Size :", len(common_ids))
        print("Catalog Scan Used : NO")
        print("-----------------------------")

        if not common_ids:
            return None

        latest_id = max(common_ids)

        return self.records[latest_id]