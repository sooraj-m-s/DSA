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
        return

    def dfs(self, node, prefix):
        if node.is_end:
            print(prefix)
        for char, child in node.children.items():
            self.dfs(child, prefix+char)

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                print("No words found with this prefix.")
                return
            node = node.children[ch]
        self.dfs(node, prefix)

    def print_words(self):
        self.dfs(self.root, '')


trie = Trie()
trie.insert('Hello World')
trie.insert('Hello Namaste')
trie.delete('Hello World')
trie.print_words()
