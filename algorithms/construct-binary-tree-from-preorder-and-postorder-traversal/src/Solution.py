# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: list, post: list) -> TreeNode:
        def construct(pre, post):
            if len(pre) == 0:
                return None
            if len(pre) == 1:
                return TreeNode(pre[0])
            root_val = pre[0]
            root_post_index = post.index(root_val)
            right_val = post[root_post_index - 1]
            right_pre_index = pre.index(right_val)

            root = TreeNode(root_val)
            root.left = construct(pre[1:right_pre_index], post)
            root.right = construct(pre[right_pre_index:], post)

            return root

        return construct(pre, post)
