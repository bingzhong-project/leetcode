> [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

# 知识点
回溯

# 解题思路
将字符串根据长度拆分成子串，构造出一颗树，然后利用回文字的判断方法控制回溯。以 "aab" 字符串为例，将有以下树被构造：
```
         S
      /  |  \
    a   aa  aab
   /    /
  a    b 
 / 
b
```

然后根据回文字的判断方法，找出符合条件的路径即可。