# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: 'TreeNode') -> 'List[int]':
        result = list()
        if root is None:
            return result
        queue = list()
        queue.append(root)

        while queue:
            # 获取每一层的末尾结点
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
