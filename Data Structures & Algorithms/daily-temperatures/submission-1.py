class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temp, index)

        # stack.append((temperatures[-1], len(temperatures)-1)) # (temp, index)
        for i, t in enumerate(temperatures):
            print(f"{i}, {t}: {stack}")
            while len(stack) != 0 and stack[-1][0] < t:
                prev_t, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((t, i))
        
        return res
        