class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        max_area = 0
        for i, cur_h in enumerate(heights):
            left_i = i
            while len(stack) > 0:
                if stack[-1][0] > cur_h:
                    seen_h, seen_i = stack.pop()
                    max_area = max(max_area, (i-seen_i)*seen_h)
                    left_i = seen_i
                else:
                    break
            stack.append((cur_h, left_i))
        
        while len(stack) > 0:
            height, ind = stack.pop()
            max_area = max(max_area, (len(heights)-ind)*height)

        return max_area