"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Approach:
        - Sliding line thing?
        """
        points = [] # (pos, is_start)
        for i in intervals:
            points.append((i.start, True))
            points.append((i.end, False))
        
        list.sort(points)
        points.append((float("inf"), False)) # just to end it

        max_rooms = 0
        cur_rooms = 0
        cur_pos = points[0][0]
        for p in points:
            if p[0] != cur_pos:
                max_rooms = max(max_rooms, cur_rooms)
                cur_pos = p[0]
            if p[1]:
                cur_rooms += 1
            else:
                cur_rooms -= 1
        
        return max_rooms