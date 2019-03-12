# Serialize and Deserialize BST

[问题描述](https://leetcode.com/problems/serialize-and-deserialize-bst/)

## 知识点

二叉搜索树

## 解题思路

将给定的字符串反序列成树，其实思路上跟题目[Construct Binary Tree from Preorder and Inorder Traversal](https://github.com/bingzhong-project/leetcode/tree/master/algorithms/construct-binary-tree-from-preorder-and-inorder-traversal) 和 题目[Construct Binary Tree from Inorder and Postorder Traversal](https://github.com/bingzhong-project/leetcode/tree/master/algorithms/construct-binary-tree-from-inorder-and-postorder-traversal) 类似。  
那么对树进行序列化时，可以按照一定格式输出其中序遍历跟前序/后序遍历，然后按照上述提到的题目的解题思路进行反序列化即可。但是题目给出的是二叉搜索树，那么很有可能可以利用 BST 的特性进行更加优雅的解题。  
根据 BST 的特性，对于任何结点 x ，其左子树的值必然比其小，右子树的值必然比其大，可以利用这个特性，作为根结点的判断。  
在序列化时，将树以先序或是后序遍历的方式转换成字符串。可以利用逗号或是其他分隔符将数值分隔，而更好的做法时将值转换为 char ，这样就不需要分隔符。  
在反序列化时，假设传入的字符串为数进行先序遍历构建的，每次将数组第一个值为根结点，该值的下一个结点为其左子结点，后面第一个比其值大的为右子结点，递归的构建树结点，构造树。
