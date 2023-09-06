# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n+= 1
            cur = cur.next
        
        w, rem = n // k, n % k
        ans = []
        cur = head
        for j in range(k):
            spaces = w + int(rem > 0)
            rem -= 1
            ans.append(cur)
            if spaces == 0:
                continue 
            i = 0
            while i < spaces - 1 and cur:
                cur = cur.next
                i += 1
            
            save_node = None
            if cur:
                save_node = cur.next
                cur.next = None
            cur = save_node
        return ans