# 1. Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

# Key

1. Using `hash map`, we store the `value: index` pair  for iteration of each elements.
2. When there are two elements paired to sum to target, return it.

# Code

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]   n
        :type target: int     
        :rtype: List[int]
        """
        table = {}
        length = len(nums)
        for i, num in enumerate(nums):
            if target - num not in table:
                table[num] = i 
            else:
                return [table[target-num], i]
        return []
        
        
```



