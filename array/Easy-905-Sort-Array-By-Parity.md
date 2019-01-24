# 905. Sort Array by Parity

Given an array `A` of non-negative integers, return an array consisting of all the even elements of `A`, followed by all the odd elements of `A`.

You may return any answer array that satisfies this condition.

 

**Example 1:**

```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

 

**Note:**

1. `1 <= A.length <= 5000`
2. `0 <= A[i] <= 5000`

# Key

- Two pointers, moving from both side of the array
- Until two pointers are not met, move pointers to even or odd index
- Exchange the value of two pointers, and move forward

Time Complexity: $O(n)$

Space Complexity: $O(1)$

# Code

```python
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        left = 0
        
        right = N-1
        while left < right and left < N:
            while left < N and A[left] % 2 == 0:
                left += 1
            while right > 0 and A[right] % 2 != 0:
                right -= 1
            if left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            print(left)
        return A
```

