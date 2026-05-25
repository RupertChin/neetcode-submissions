# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev_node = None
        cur_node = None
        next_node = head

        while next_node is not None:
            prev_node = cur_node
            cur_node = next_node
            next_node = cur_node.next

            cur_node.next = prev_node
        
        return cur_node

        # prev_node = None
        # cur_node = head

        # while cur_node:
        #     next_node = cur_node.next
        #     cur_node.next = prev_node
        #     prev_node = cur_node
        #     cur_node = next_node
        
        # return prev_node
