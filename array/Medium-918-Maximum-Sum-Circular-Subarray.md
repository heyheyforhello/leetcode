# Key

The max sum of circular array is either:

1. The max subarray without circle
2. The max subarray with circle, but can be complemented with min subarray.

![](https://assets.leetcode.com/users/motorix/image_1538888300.png)

# Code

```python
class Solution:
    def maxSubarraySumCircular(self, A):
        total = 0
        curMin = 0
        curMax = 0
        maxSum = -2**32
        minSum = 2**32
        for a in A:
            total += a
            curMax = max(curMax+a, a)
            maxSum = max(curMax, maxSum)
            curMin = min(curMin+a, a)
            minSum = min(curMin, minSum)
        if maxSum < 0:
            return maxSum
        else:
            return max(total - minSum, maxSum)
```