class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        current_node = self.root
        for i in word:
            if i not in current_node.children:
                current_node.children[i] = Node()
            current_node = current_node.children[i]
        current_node.is_end = True
    
    def search(self, word):
        current_node = self.root
        for i in word:
            if i not in current_node.children:
                return False
            current_node = current_node.children[i]
        return current_node.is_end
    
    def delete(self, word):
        current_node = self.root
        for i in word:
            if i not in current_node.children:
                return False
            current_node = current_node.children[i]
        current_node.is_end = False

    def _dfs(self, node, prefix):
        if node.is_end:
            print(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix+char)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                print("No words found with this prefix.")
                return
            node = node.children[ch]
        self._dfs(node, prefix)

    def print_words(self):
        self._dfs(self.root, '')




if __name__ == "__main__":
    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Example usage
    trie = Trie()
    trie.insert('Hello World')
    trie.insert('Hello Namaste')
    trie.insert('Welcome')
    # trie.delete('Hello World')
    trie.print_words()

