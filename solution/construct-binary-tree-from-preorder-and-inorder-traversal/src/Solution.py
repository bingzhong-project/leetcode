# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def dfs(preorder, inorder):
            if len(preorder) == 0:
                return None
            val = preorder[0]
            root = TreeNode(val)
            if val not in inorder:
                return None
            else:
                preorder.pop(0)
            index = inorder.index(val)
            root.left = dfs(preorder, inorder[:index])
            root.right = dfs(preorder, inorder[index + 1:])
            return root

        return dfs(preorder, inorder)
