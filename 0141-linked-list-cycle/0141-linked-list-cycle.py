# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = next_position = head
        if head == None:
            return False
        while next_position and next_position.next:
            cur = cur.next
            next_position = next_position.next.next
            if cur == next_position:
                return True
        return False