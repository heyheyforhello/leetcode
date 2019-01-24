# [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/)

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a *move* consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

**Example 1:**

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
```

**Example 2:**

```
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
```

**Example 3:**

```
Input: stones = [[0,0]]
Output: 0
```

# Key




# Code


```python
class Solution():
    def removeStones(self, points):
        N = len(points)
        self.table = {}
        def find(item):
            if item != self.table[item]:
                self.table[item] = find(self.table[item])
            return self.table[item]
        
        def union(x, y):
            self.table.setdefault(x, x)
            self.table.setdefault(y, y)
            self.table[find(x)] = find(y)
        
        for x, y in points:
            union(x, ~y)
        return N - len({find(x) for x in self.table})



solution = Solution()
solution.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
```