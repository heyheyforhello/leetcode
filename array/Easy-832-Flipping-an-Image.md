# 832. Flipping an Image

Given a binary matrix `A`, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping `[1, 1, 0]` horizontally results in `[0, 1, 1]`.

To invert an image means that each `0` is replaced by `1`, and each `1` is replaced by `0`. For example, inverting `[0, 1, 1]` results in `[1, 0, 0]`.

**Example 1:**

```
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
```

**Example 2:**

```
Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
```

**Notes:**

- `1 <= A.length = A[0].length <= 20`
- `0 <= A[i][j] <= 1`

# Key

- Easy, no explanation

Time complexity: $O(n)$

Space complexity: $O(1)$

# Code

```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(A)
        M = len(A[0])
        
        for i in range(N):
            for j in range(M//2):
                A[i][j], A[i][M-j-1] = A[i][M-j-1], A[i][j]
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
                if A[i][M-j-1] == 0:
                    A[i][M-j-1] = 1
                else:
                    A[i][M-j-1] = 0
            print(A)
        if M%2 != 0:
            for i in range(N):
                if A[i][M//2] == 0:
                    A[i][M//2] = 1
                else:
                    A[i][M//2] = 0
        return A

# Better solution
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        k = n//2
        for row in A:
            for i in range(k):
                if row[i] == row[n-i-1]:
                    row[i] ^= 1
                    row[n-i-1] = row[i]
            if n % 2:
                row[k] ^=1
        return A
```

