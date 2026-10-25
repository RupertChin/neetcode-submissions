# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Approach:
        - 2 pointers, find midpoint
        - reverse second half, merge lists
        """

        print("START")

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print("SPLIT HALF")
        
        second = slow.next
        # reverse second half linked list
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev
        print("REVERSE SECOND HALF")

        # merge linked list
        cur_node = head

        while second:
            next_node = cur_node.next
            second_next = second.next

            cur_node.next = second
            second.next = next_node

            cur_node = next_node
            second = second_next

        print("MERGED LINKED LIST")

        



        
            
