# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        linkedListSize = 0
        cur = head
        while cur:
            linkedListSize += 1
            cur = cur.next
        
        needRemove = linkedListSize - n
        ans = ListNode()
        ans.next = head
        cur = ans
        for _ in range(needRemove):
            cur = cur.next
        nextHead = None
        cur.next = cur.next.next
        return ans.next
            