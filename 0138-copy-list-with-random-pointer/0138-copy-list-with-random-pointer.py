"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, nxt, curr.random)
            curr = nxt
        
        origin = head
        while origin:
            copy = origin.next
            if origin.random:
                copy.random = origin.random.next
            origin = copy.next # next origin
            
        origin = head
        copy_head = head.next
        copy_prev = None
        while origin:
            copy = origin.next
            if copy_prev:
                copy_prev.next = copy
            origin.next = copy.next
            copy_prev = copy
            origin = origin.next # next origin 

        return copy_head