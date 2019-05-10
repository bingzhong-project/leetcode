# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        res = []
        queue = []
        if root:
            queue.append(root)
        while queue:
            res.append([])
            for _ in range(len(queue)):
                node = queue.pop(0)
                res[-1].append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)
        return res
