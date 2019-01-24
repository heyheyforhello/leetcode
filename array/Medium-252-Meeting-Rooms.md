a# 252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` $(s_i < e_i)​$, determine if a person could attend all meetings.

**Example 1:**

```
Input: [[0,30],[5,10],[15,20]]
Output: false
```

**Example 2:**

```
Input: [[7,10],[2,4]]
Output: true
```

# Key

1. Sort the start times and end times.
2. Once any start time is later than next end time, we determine it as invalid, `return false`.
3. Else if all intervals do not collide each other, `return true`.

# Coder

```python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        starts = []
        ends = []
        N = len(intervals)
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        
        for i in range(1, N):
            if starts[i] < ends[i-1]:
                return False
        return True
        
```

