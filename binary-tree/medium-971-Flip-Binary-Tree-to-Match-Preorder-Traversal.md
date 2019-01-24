# 971 Flip Binary Tree To Match Preorder Traversal

Given a binary tree with `N` nodes, each node has a different value from `{1, ..., N}`.

A node in this binary tree can be *flipped* by swapping the left child and the right child of that node.

Consider the sequence of `N` values reported by a preorder traversal starting from the root.  Call such a sequence of `N` values the *voyage* of the tree.

(Recall that a *preorder traversal* of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the **least number** of nodes in the tree so that the voyage of the tree matches the `voyage` we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list `[-1]`.

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/01/02/1219-01.png)**

```
Input: root = [1,2], voyage = [2,1]
Output: [-1]
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)**

```
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2019/01/02/1219-02.png)**

```
Input: root = [1,2,3], voyage = [1,2,3]
Output: []
```

 

**Note:**

1. `1 <= N <= 100`

# Key

With DFS, we traverse the tree in pre-order. Besides, we should keep a global variable to memorize our position in `voyage` array. in every traversal, we could meet the following situations:

If the value of root equals to current voyage element:

1. If the value of left element equals next voyage element, continue traversing
2. If the value of right element equals next voyage element, reverse the order and traverse
   - If the left node exists, we should add it to `res` array, then we proceed the reversed traversal

else, any error will trigger `return False` statement, to tell the traversal that this is a bad tree: `return False`

After the above calculations, we see if the response of DFS is False. If it is valid, the response will be `True`, and we should return the `res` array

# Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        # global variable to iterate voyage
        self.next = 0
        res = []
        def dfs(root):
            if not root: return True
            if root.val != voyage[self.next]: return False
            self.next += 1
            if root.left and root.left.val == voyage[self.next]:
                return dfs(root.left) and dfs(root.right)
            elif root.right and root.right.val == voyage[self.next]:
                # the right root equals next, while we have left, we reverse it
                if root.left: res.append(root.val)
                # since right root is reversed, we traverse in different direction
                return dfs(root.right) and dfs(root.left)
            # if left and right are none, return True
            return root.left == root.right == None
        return res if dfs(root) else [-1]
```

