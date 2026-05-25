# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthRecursion(self, curr: Optional[ListNode], n):
        if not curr.next:
            return 1
        
        num_following = self.removeNthRecursion(curr.next, n)

        if num_following == n:
            # do stuff then return n+1 so nothing else happens
            curr.next = curr.next.next
        
        return num_following + 1

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head

        self.removeNthRecursion(temp, n)

        return temp.next
        