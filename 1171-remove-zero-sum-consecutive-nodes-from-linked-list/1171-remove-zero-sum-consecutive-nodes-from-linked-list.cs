/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveZeroSumSublists(ListNode head) {
        ListNode root = new ListNode(0, head);
        int prefix = 0;
        Dictionary<int,ListNode> prefixMap= new Dictionary<int,ListNode>(); 
        for (ListNode current = root; current != null; current = current.next) {
            prefix += current.val;
            prefixMap[prefix] = current;
        }
        
        prefix = 0;
        for (ListNode current = root; current != null; current = current.next) {
            prefix += current.val;
            current.next = prefixMap[prefix].next;
        }
        
        return root.next;
    }
}