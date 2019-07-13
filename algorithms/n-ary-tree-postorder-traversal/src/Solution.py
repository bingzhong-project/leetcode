# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> 'List[int]':
        def post(node, res):
            if node:
                for c in node.children:
                    post(c, res)
                res.append(node.val)

        res = []
        post(root, res)

        return res
