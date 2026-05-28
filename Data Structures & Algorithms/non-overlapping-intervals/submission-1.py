class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Approach:
        sort intervals array
        - when overlap detected, increment counter
        - we can ensure an optimal solution by always removing the first overlap
        - instead of directly comparing the intervals, track the last ending val
        issue: earlier start but later end situation
        - fix: order by end first? or iterate backwards?
        """

        list.sort(intervals)

        num_remove = 0
        last_start = float("inf")

        for interval in reversed(intervals):
            if interval[1] > last_start:
                num_remove += 1
            else:
                last_start = interval[0]
        
        return num_remove