class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # if len(intervals) == 1:
        #     res.append(intervals[0])
        #     return res

        list.sort(intervals)

        i = 0
        while i < len(intervals):
            # print(f"index {i}")
            if i < len(intervals) - 1 and intervals[i][1] >= intervals[i+1][0]:
                start = intervals[i][0]
                end = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = [start, end]
                # res.append([start, end])
                # i += 1
            else:
                res.append(intervals[i])
            i += 1
        
        return res