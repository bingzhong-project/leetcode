> [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

# 知识点
树的先序遍历，栈

# 解题思路
使用非递归的方式完成树的先序遍历。根据先序遍历的规律，使用栈来完成。  
在开始迭代前，先将根节点入栈，之后在迭代中，弹出位于栈顶的节点，即表示遍历到该节点，然后依次将该节点的右节点和左节点。当栈中没有元素时，即表示完成遍历。