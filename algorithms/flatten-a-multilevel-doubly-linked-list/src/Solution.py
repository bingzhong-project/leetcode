# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        sentinel = Node(None, None, None, None)
        sentinel.child = head
        node = head
        while node:
            next_node = node.next
            if node.child:
                new_node = self.flatten(node.child)
                node.child = None
                next_node = node.next
                node.next = new_node
                new_node.prev = node
                last_node = new_node
                if next_node:
                    while last_node:
                        next_node.prev = last_node
                        last_node = last_node.next
                    next_node.prev.next = next_node
            node = next_node

        return sentinel.child
