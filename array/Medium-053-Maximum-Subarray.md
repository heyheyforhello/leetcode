# Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Key

- If the current sum is non-negative, add it to current value
- or else, the current value will be the best current sum
- Each time, we select the best out of all the iterations.

Time complexity: $O(n)$

Space complexity: $O(1)$

# Code

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case: all input below 0
        if nums==[]: return None
        maxSum=nums[0]
        thisSum=0
        for j in nums:
            thisSum+=j
            if thisSum>maxSum:
                maxSum=thisSum
            if thisSum<0:
                thisSum=0
        return maxSum

# Cleaner solution
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = 0
        maxSum = -2**32
        for i, num in enumerate(nums):
            curMax = max(num, curMax+num)
            maxSum = max(curMax, maxSum)
        
        return maxSum
```

