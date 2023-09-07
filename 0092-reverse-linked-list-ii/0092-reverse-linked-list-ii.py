class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        prev = ListNode(0, head)
        temp = prev
        for _ in range(left - 1):
            prev = prev.next
        
        cur = prev.next
        
        for _ in range(right - left):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return temp.next