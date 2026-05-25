# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 1:
        - iterate through every linkedlist head, tracking index of lowest value
        - take from that linkedlist until all heads are null
        Approach 2:
        - merge 2 linkedlists at a time, continuing until only 1 remains
        """
        if len(lists) == 0: 
            return None

        while len(lists) > 1:
            # merge lists[-1] and lists[-2]
            list1 = lists.pop()
            list2 = lists.pop()
            merged = ListNode()
            temp = merged
            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = list1
                    temp = temp.next
                    list1 = list1.next
                else:
                    temp.next = list2
                    temp = temp.next
                    list2 = list2.next
            if list1:
                temp.next = list1
            elif list2:
                temp.next = list2
            
            lists.append(merged.next)
        
        return lists[0]
