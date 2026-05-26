class TrieNode:
    val: str
    is_terminal: bool
    children: dict

    def __init__(self, c: str = "", t: bool = False):
        self.val = c
        self.is_terminal = t
        self.children = {}

class PrefixTree:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for i, char in enumerate(word):
            if char not in curNode.children:
                curNode.children[char] = TrieNode(char)
            if i == len(word) - 1:
                curNode.is_terminal = True
            curNode = curNode.children[char]


    def search(self, word: str) -> bool:
        curNode = self.root
        for i, char in enumerate(word):
            if char not in curNode.children:
                return False
            if i < len(word) - 1:
                curNode = curNode.children[char]

        print(f"searching {word}, {curNode.is_terminal}")
        return curNode.is_terminal

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for i, char in enumerate(prefix):
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        
        return True
        