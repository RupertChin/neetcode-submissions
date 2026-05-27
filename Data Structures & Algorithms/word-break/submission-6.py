class TrieNode:
    val: str
    is_terminal: bool
    children: dict

    def __init__(self, v: str = ""):
        self.val = v
        self.is_terminal = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach:
        - dp problem, multiple words can have same prefix
            - either select one or other
        - trie? more efficient lookup
            - search per char, recursive call per terminal node
            - top down, memoization
        """

        # build trie
        trie = TrieNode()
        for word in wordDict:
            curr = trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode(c)
                curr = curr.children[c]
            curr.is_terminal = True
        
        mem = [None] * (len(s) + 1) # is memoization really required?
        def _wordBreak(i: int) -> bool:
            # do stuff

            if i == len(s):
                return True

            # need memoization check? 
            if mem[i] is not None:
                return mem[i]
            
            cur_node = trie
            while i < len(s) and s[i] in cur_node.children:
                cur_node = cur_node.children[s[i]]
                i += 1
                if cur_node.is_terminal:
                    if _wordBreak(i):
                        mem[i] = True
                        return True
            
            mem[i-1] = False
            return False
        
        return _wordBreak(0)
