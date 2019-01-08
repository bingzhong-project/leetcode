# Symmetric Tree

[问题描述](https://leetcode.com/problems/symmetric-tree/)

## 知识点

广度优先搜索，深度优先搜索

## 解题思路

### 广度优先搜索解法

逐层处理，所以需要知道何时遍历了一层，使用一个末尾指针 last，指向每层的最后一个节点。每次队列中元素出队，都判断是否于 last 节点相等，如果是则表示上一层的最后一个节点出队，此时队尾的节点为该层的最后一个节点，last 指针指向该节点。  
在遍历的同时，利用一个数组 paths 收集同层节点，当该层的最后一个节点出队时，判断数组是否为左右对称数组，以此判断树是否为左右对称树。

### 深度优先搜索解法

思路参考：[Symmetric Tree Solution](https://leetcode.com/problems/symmetric-tree/solution/)
