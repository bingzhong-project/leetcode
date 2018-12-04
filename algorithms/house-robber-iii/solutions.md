> [House Robber III](https://leetcode.com/problems/house-robber-iii/description/)

# 知识点
深度优先搜索

# 解题思路
每个节点都有两种状态，偷与不偷。从树的叶子节点开始进行遍历，算出每个节点如果偷的话，最大收益是多少，不偷的话，最大收益又是多少。  
如果一个节点选择偷，那么它的最大收益为当前节点的值加上其子节点不偷的值，选择不偷的话，其最大收益为左节点的最大收益加上右节点的最大收益（规则只是邻层的节点不能同时进行偷取，但是同一层的节点无所谓偷与不偷），如果节点没有子节点，则以收益为 0 的节点作为其子节点。可以得出每个节点的收益公式：
```python
node.steal = node.val + node.left.not_steal + node.right.not_steal
node.not_steal = max(node.left.steal, node.left.not_steal) + max(node.right.steal, node.right.not_steal)
```
在编程时，可以自己定义一组数据结构，也可以利用数组来表示节点偷与不偷的最大值。