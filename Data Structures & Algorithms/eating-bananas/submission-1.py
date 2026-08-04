import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_rate(cur_min, cur_max):
            # print(f"{cur_min}, {cur_max}")
            if cur_min > cur_max: 
                return -1
            cur_rate = (cur_min + cur_max) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / cur_rate)
            
            if t > h:
                return find_rate(cur_rate+1, cur_max)
            else:
                x = find_rate(cur_min, cur_rate-1)
                if x != -1:
                    return x
                else:
                    return cur_rate
            
            # return cur_rate
        return find_rate(1, max(piles))