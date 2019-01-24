# Description

Given an array `nums` of *n* integers and an integer `target`, are there elements *a*, *b*, *c*, and *d* in `nums` such that *a* + *b* + *c* + *d* = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

**Note:**

The solution set must not contain duplicate quadruplets.

**Example:**

```
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

# Key

- Pick up two pointers from left to right,
- Search rest combinations with two pointer method

The time complexity: $O(n^3)$

The space complexity: $O(1)$

# Code

```python
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNSum(l, r, target,N, result, results):
            # Terminate early
            if N < 2 or r-l+1 < N or target < nums[l]*N or nums[r]*N < target:
                return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result+[nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            # Recursively reduce
            else:
                for i in range(l, r+1):
                    if i == l or (i>l and nums[i-1] != nums[i]):
                        findNSum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
            
        nums.sort()
        results = []
        findNSum(0, len(nums)-1, target, 4, [], results)
        return results
```

