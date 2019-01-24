# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Sum = 0
        carry = 0
        cur1 = l1
        cur2 = l2
        prev = None
        while cur1 and cur2:
            Sum = cur1.val + cur2.val + carry
            carry = Sum//10
            cur1.val = Sum%10
            prev = cur1
            cur1 = cur1.next
            cur2 = cur2.next

        cur = None
        if cur2:
            cur = cur2
        elif cur1:
            cur = cur1
        
        Sum = 0
        while cur:
            Sum = cur.val + carry
            carry = Sum//10
            prev.next = ListNode(Sum%10)
            prev = prev.next
            cur = cur.next

        if carry:
            prev.next = ListNode(carry)
        return l1
        