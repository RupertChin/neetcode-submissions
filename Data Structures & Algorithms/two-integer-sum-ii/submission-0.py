class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (s := numbers[l] + numbers[r]) != target:
            if s < target:
                l += 1
            else:
                r -= 1
        
        return [l + 1, r + 1]