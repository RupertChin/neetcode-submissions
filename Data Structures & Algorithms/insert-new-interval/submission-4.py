class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Approach:
        - iterate through intervals until start >= new start
            - save this position
        - check for overlap: continue iterating
            - any interval with overlap, combine ranges into new interval
            - remove the old overlapping interval
        - insert the new interval at the initially saved position
        """

        pos = len(intervals)
        for i in range(len(intervals)):
            print(f"checking index {i}")
            if intervals[i][0] >= newInterval[0]:
                print(f"insert here")

                # check intervals after
                while i < len(intervals) and intervals[i][0] <= newInterval[1]:
                    print(f"merge next interval: {intervals[i]}")
                    newInterval[1] = max(newInterval[1], intervals[i][1])
                    del intervals[i]
                    print(intervals)

                pos = i
                break

        # check interval before
        print(f"check prev: {pos} | {intervals}")
        if pos > 0 and intervals[pos-1][1] >= newInterval[0]:
            print(f"merge prev interval: {intervals[i-1]}")
            newInterval[0] = intervals[pos-1][0]
            newInterval[1] = max(newInterval[1], intervals[pos-1][1])
            del intervals[pos-1]
            pos -= 1
            print(intervals)
        
        intervals.insert(pos, newInterval)
        return intervals