# [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)

Given a string **s** , find the length of the longest substring **t**  that contains **at most** 2 distinct characters.

**Example 1:**

```
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
```

**Example 2:**

```
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
```

# Key
Construct a sliding window, with slow/fast pointer. The slow pointer points to the start of substring, while the fast pointer points to the end of substring. 

- Compare the current length with max length, and get the longest substring.
- After the comparison, move the slow pointer to fast pointer, and move the fast pointer to next position.
- When we reach the end of string, there could be two condition: the fast pointer did not find next different character, or fast pointer find the next different charater. We should take care of this situation as special case.


# Code

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N <= 2:
            return N
        res = 0
        i, l, r = 0, 0, 1
        while i < N:
            # Move fast pointer to next different character
            while r < N and s[l] == s[r]:
                r += 1
            
            if r+1<N:                     # The border of different character does not reach the end
                i = r+1
            elif r == N-1:
                return max(r-l+1, res)    # The pointer reached the end of string
            elif r == N:
                return max(r-l, res)      # The pointer reached the end while not found different charater

            
            while i < N and (s[i] == s[l] or s[i] == s[r]):
                i += 1
            
            res = max(res, i-l)
            l = r
            r = r+1
        return res
        
        
solution = Solution()
print(solution.lengthOfLongestSubstringTwoDistinct("aaaa"))
```