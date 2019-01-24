# 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

# Key



# Code

```python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        starts, ends = [], []
        N = len(intervals)
        res = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        
        i = 0
        for j in range(1, N):
            if starts[j] > ends[j-1]:
                res.append([starts[i], ends[j-1]])
                i = j
        res.append([starts[i], ends[N-1]])
            
                
        return res
        
```

