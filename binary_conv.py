# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
       stack=[]
       d=0
       while head:
        stack.append(head.val)
        head=head.next
       n=len(stack)
       for i in range(n):
        d=d+stack.pop()*(2**i)
       return d