from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        bracketValues = {
            '(': 1,
            ')': -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        stack = deque()

        for c in s:
            # print("checking: " + c)
            if bracketValues[c] > 0:
                # print("opening bracket")
                stack.append(bracketValues[c])
            else:
                # print("closing bracket")
                if len(stack) == 0 or bracketValues[c] != stack.pop()*-1:
                    return False
        
        return len(stack) == 0
            
