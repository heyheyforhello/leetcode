# 3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

**Example 1**:
```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

```
**Example 2**:
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```
**Example 3**:
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
# Key
- Variable `start_index` to record the current starting point
- Variable `cur_len`: record the current length of string
- Variable `max_len`: record the maximum length of string
- Variable `table`: record the newest position of characters
  
From left to right, once duplicate characters are found, shorten the string so that the string is not duplicated, and update the new length.
# Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        cur_len = 0
        start_index = 0
        table = {}
        for i, c in enumerate(s):
            if c not in table:
                cur_len += 1
                table[c] = i
            else:
                if start_index > table[c]:
                    cur_len += 1
                else:
                    start_index = table[c] + 1
                cur_len = i - start_index + 1
                table[c] = i
            max_len = max(cur_len, max_len)
        return max_len
```