# Description



# Code
```python
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.N = len(s)
        self.maxLength = 0
        self.res = ""
        def extendPalindrome(i, j):
            while i >= 0 and j < self.N:
                if s[i] != s[j]:
                    break
                else:
                    i -= 1
                    j += 1
            if self.maxLength < j-i:
                self.maxLength = j-i
                self.res = s[i+1:j]
        
        
        for i in range(self.N):
            extendPalindrome(i,i)
            extendPalindrome(i, i+1)
        
        return self.res
```