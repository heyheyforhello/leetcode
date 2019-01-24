# 15. 3Sum

Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:**

The solution set must not contain duplicate triplets.

**Example:**

```
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

# Key

1. Sort the array
2. Element `i` iterate from left to right, while `j` move from `i+1` to right, `k` move from last element to left.
3. All possible combinations are constructed as `j` meet `k` for element `i`.
4. Noting that skipping duplicates require some extra efforts

# Code

```python
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        res = []
        nums.sort()
        i = 0
        for i, num in enumerate(nums):
            left = i+1
            right = length-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                s = num + nums[left] + nums[right]
                
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    
                    res.append([num, nums[left], nums[right]])
                    # skip duplicate elements
                    while left < right-1 and nums[left] == nums[left+1]:
                        left += 1
                    while right > left+1 and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
```

