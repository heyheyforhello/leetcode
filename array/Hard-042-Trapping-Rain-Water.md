# Description
# Key
# Code
```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        water = 0
        for i, h in  enumerate(height):
            while stack and stack[-1][1] < h:
                low = stack.pop()
                lowHeight = low[1]
                if stack:
                    leftHigh = stack[-1][1]
                    leftIndex = stack[-1][0]
                    water += (min(leftHigh, h) - lowHeight)*(i-leftIndex-1)
                
            stack.append([i, h])
        print(water)
            
solution = Solution()
solution.trap([5, 1, 1, 1, 1, 5])
```