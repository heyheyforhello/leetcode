

# 83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only *once*.

**Example 1:**

```
Input: 1->1->2
Output: 1->2
```

**Example 2:**

```
Input: 1->1->2->3->3
Output: 1->2->3
```

# Key

1. Keep two pointer to `prev` and `cur`.
2. If value of two pointers are different, move forward the two pointers

3. If value of two pointers are same, remove `cur` from linked list.

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev = head
        cur = head.next
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head
```

