# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        def pre(node, res):
            if node is not None:
                res.append(node.val)
                for c in node.children:
                    pre(c, res)

        res = []
        pre(root, res)

        return res
