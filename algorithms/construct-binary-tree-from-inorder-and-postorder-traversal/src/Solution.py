# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def construct(postorder, inorder):
            if len(postorder) == 0:
                return None
            val = postorder[-1]
            if val not in inorder:
                return None
            else:
                postorder.pop()
            index = inorder.index(val)
            root = TreeNode(val)
            root.right = construct(postorder, inorder[index + 1:])
            root.left = construct(postorder, inorder[:index])
            return root

        return construct(postorder, inorder)
