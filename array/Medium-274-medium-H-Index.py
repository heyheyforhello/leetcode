class Solution:
    # Bucket sort solution
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        N = len(citations)
        bucket = [0] *( N+1)
        for cite in citations:
            if cite > N:
                bucket[N] += 1
            else:
                bucket[cite] += 1
        count = 0
        for i in reversed(range(N+1)):
            count += bucket[i]
            if count >= i:
                return i
        return 0
        