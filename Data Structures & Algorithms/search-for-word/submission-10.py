class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findword(row, col, i):
            nonlocal board, word

            # if i >= len(word):
            #     return True

            # if row >= len(board) or row < 0: 
            #     return False
            # if col >= len(board[0]) or col < 0:
            #     return False

            cur_char = board[row][col]
            if cur_char == word[i]:
                # print(f"cur_char: {cur_char}")
                if i == len(word) - 1:
                    return True
                board[row][col] = '*'
                if row+1 < len(board) and board[row+1][col] != '*' and findword(row+1, col, i+1):
                    # print("going down")
                    return True
                if row-1 >= 0 and board[row-1][col] != '*' and findword(row-1, col, i+1):
                    # print("going up")
                    return True
                if col+1 < len(board[0]) and board[row][col+1] != '*' and findword(row, col+1, i+1):
                    # print("going right")
                    return True
                if col-1 >= 0 and board[row][col-1] != '*' and findword(row, col-1, i+1):
                    # print("going left")
                    return True
                board[row][col] = cur_char
            
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                x = findword(row, col, 0)
                # print(f"checking {board[row][col]}: {x}")
                if x:
                    return True
        
        return False