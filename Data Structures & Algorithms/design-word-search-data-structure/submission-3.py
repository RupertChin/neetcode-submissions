class TrieNode:
    val: str
    is_terminal: bool
    children: dict

    def __init__(self, val: str = "", is_terminal: bool = False):
        self.val = val
        self.is_terminal = is_terminal
        self.children = {}
    
    def search(self, word: str, i: int) -> bool:
        # if i == len(word) - 1 and not self.is_terminal:
        #     return False
        if i == len(word):
            return self.is_terminal

        cur_char = word[i]
        if cur_char != '.':
            if cur_char not in self.children:
                return False
            return self.children[cur_char].search(word, i+1)
        else:
            for node in self.children.values():
                if node.search(word, i+1):
                    return True
            return False

class WordDictionary:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode(char)
            cur_node = cur_node.children[char]
        cur_node.is_terminal = True

    def search(self, word: str) -> bool:
        return self.root.search(word, 0)

"""
Approach:
Implement a trie
- for '.', recursively call itself for every child at that node
"""