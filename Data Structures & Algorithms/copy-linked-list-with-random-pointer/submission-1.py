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
        if not head:
            return None

        cur = head
        otw = {}

        while cur:
            otw[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                otw[cur].next = otw[cur.next]
            if cur.random:
                otw[cur].random = otw[cur.random]
            cur = cur.next

        return otw[head]

        