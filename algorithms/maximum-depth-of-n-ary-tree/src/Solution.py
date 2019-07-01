# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        depth = 0
        queue = []
        if root:
            queue.append(root)
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                for child in node.children:
                    queue.append(child)
        return depth
