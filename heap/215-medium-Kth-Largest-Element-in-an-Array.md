# 215. Kth Largest Element in an Array

Find the **k**th  largest element in an unsorted array. Note that it is the kth largest  element in the sorted order, not the kth distinct element.

**Example 1:**

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:** 
 You may assume k is always valid, 1 ≤ k ≤ array's length.

# Key

Partition Solution: best time $O(N)$, worst time $O(N^2)$

# Code

```python
# partition solution
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(lo, hi):
            i = lo+1
            j = hi
            while True:
                while nums[i] < nums[lo]:
                    i += 1
                while nums[j] >= nums[lo]:
                    j -= 1
                if i >= j:
                    break
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[j], nums[lo] = nums[lo], nums[j]
            return j

        N = len(nums)
        k = N - k
        lo = 0
        hi = N-1
        while lo < hi:
            j = partition(lo, hi)
            if j < k:
                lo = j+1
            elif j > k:
                hi = j
            else:
                break
        print(nums[k])
        return nums[k]
```

```python
class Solution:
    # Heap solution
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        N = len(nums)
        for num in nums:
            heapq.heappush(heap, num)
        k = N-k+1
        while k:
            res = heapq.heappop(heap)
            k -= 1
        return res
```

