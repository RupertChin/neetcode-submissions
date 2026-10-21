class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        what if you just tread the 2d array as 1d? flatten the jit
        row = ind // rows
        col = ind % rows
        """
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while (l <= r):
            mid = (l + r) // 2
            mid_val = matrix[mid//cols][mid%cols]
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False