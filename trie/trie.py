from trie.trie_node import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, title, data):
        node = self.root
        for char in title.lower(): # Case insensitive
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.movie_data = data
    
    def _dfs(self, node, results):
        if node.is_end:
            results.append(node.movie_data)
        for char in node.children:
            self._dfs(node.children[char], results)

    def search_exact(self, title):
        node = self.root
        for char in title.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node.movie_data if node.is_end else None

    def starts_with(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        
        
        results = []
        self._dfs(node, results)
        return results

