"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}

        if not head:
            return None 
            
        copy_head = Node(head.val)
        node_map[head] = copy_head

        cur = head
        while cur.next:
            copy_next = Node(cur.next.val)
            node_map[cur].next = copy_next

            node_map[cur.next] = copy_next
            
            cur = cur.next
        
        # fill the random pointers
        cur = head
        while cur:
            node_map[cur].random = node_map[cur.random]
            cur = cur.next
        
        return node_map[head]
        