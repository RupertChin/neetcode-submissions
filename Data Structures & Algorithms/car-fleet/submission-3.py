class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        # stack = [] # stack of r atios

        prev_ratio = -1
        for pos, speed in reversed(sorted(list(zip(position, speed)))):
            cur_ratio = (target - pos) / speed

            if cur_ratio <= prev_ratio:
                res -= 1
            else:    
                prev_ratio = cur_ratio
                
        
        return res