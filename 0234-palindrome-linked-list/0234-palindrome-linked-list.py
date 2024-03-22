# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        cur, prevNode,nextNode = root, None ,ListNode() 
        while cur != None:
            nextNode = cur.next
            cur.next = prevNode
            prevNode = cur
            cur = nextNode
        
        return prevNode
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        root = head
        s, f = head, head
        if not head or not head.next:
            return True
        while f and f.next:
            f = f.next.next
            s = s.next
        reversedList = self.reverseList(s)
        
        cur = root
        while cur != None and reversedList != None:
            if (cur.val != reversedList.val):
                return False
            reversedList = reversedList.next
            cur = cur.next
        return True