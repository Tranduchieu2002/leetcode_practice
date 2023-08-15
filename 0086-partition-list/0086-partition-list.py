# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first_list, second_list = ListNode(), ListNode()
        cur_first_node, cur_second_node = first_list, second_list
        while(head):
            if head.val < x:
                cur_first_node.next = ListNode(head.val)
                cur_first_node = cur_first_node.next
            else:
                cur_second_node.next = ListNode(head.val)
                cur_second_node = cur_second_node.next
            head = head.next
        cur_first_node.next = second_list.next
        return first_list.next