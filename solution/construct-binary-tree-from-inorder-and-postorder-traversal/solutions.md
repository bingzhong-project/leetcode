> [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

# 知识点
中序遍历，后序遍历

# 解题思路
总的思路和 [Construct Binary Tree from Preorder and Inorder Traversal 解题思路](https://gitee.com/bingzhong-project/leetcode/blob/master/solution/construct-binary-tree-from-preorder-and-inorder-traversal/solutions.md) 基本一致，只不过根据后序遍历的特性更改了数组的访问顺序。而后序遍历的访问顺序刚好与前序遍历的访问顺序相反。  
后序遍历顺序：  
![DFS Postorder](https://bingzhong-project.gitee.io/public/pictures/dfs-postorder.png)