# Minimum Height Trees

[问题描述](https://leetcode.com/problems/minimum-height-trees/)

参考资料：[Minimum Height Trees Discuss](https://leetcode.com/problems/minimum-height-trees/discuss/76055/share-some-thoughts)

## 知识点

深度优先搜索，图

## 解题思路

由于问题只给出了边，所以首先要将图转化为邻接表。

### 广度优先搜索

首先是通过利用广度优先搜索来进行解答，广度优先搜索能够找出任意结点 u 到结点 v 的最短距离，利用这个特性计算出所有结点作为根节点时的树的高度，然后找出最小的高度。当然这种解法本质上为穷举，没办法过到最后几个的 Testcase 。

### 图

另外一种解法是从叶子结点开始数结点。  
首先找出所有的叶子结点，然后一个个的删除掉叶子结点，之后会有新的叶子结点，再删除，当结点只剩下 1 ~ 2 个时，这些结点就是答案。
