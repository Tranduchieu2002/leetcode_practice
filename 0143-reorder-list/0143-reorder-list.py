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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        cur = head
        while cur:
            st.append(head)
            cur = cur.next
        
        
        slow , fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        cur = slow
        prev, next = None, None
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        first_half, second_half = head, prev
        while second_half.next:  # second_half is shorter or equal length to first_half
            next_first = first_half.next
            next_second = second_half.next
            
            first_half.next = second_half
            second_half.next = next_first
            
            first_half = next_first
            second_half = next_second