# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        node = head
        copies = {}
        while node:
            if node.val not in copies:
                copies[node.val] = Node(node.val, None, None)
            next = node.next
            random = node.random
            if next and next.val not in copies:
                copies[next.val] = Node(next.val, None, None)
            if random and random.val not in copies:
                copies[random.val] = Node(random.val, None, None)

            copies[node.val].next = copies[next.val] if next else None
            copies[node.val].random = copies[random.val] if random else None
            node = node.next

        return copies[head.val]
