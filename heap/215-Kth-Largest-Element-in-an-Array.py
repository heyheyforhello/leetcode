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
    # second solution by heap
    def findKthLargest1(self, nums, k):
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
        
            
solution = Solution()
solution.findKthLargest([1], 1)
