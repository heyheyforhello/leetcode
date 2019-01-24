# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            
            if node1.left and node1.right and node2.left and node2.right and node1.left.val == node2.right.val:
                return dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
            elif node1.left and node2.right and node1.left.val == node2.right.val:
                return dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
            elif node1.right and node2.left and node1.right.val == node2.left.val:
                return dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            
        return dfs(root1, root2)
                