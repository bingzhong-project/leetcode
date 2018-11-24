> [House Robber](https://leetcode.com/problems/house-robber/description/)

# 知识点
动态规划

# 解题思路
对于每间屋子来说，都有偷或者不偷两种选择。如果选择偷的话，对于上一间房子只能选择不偷，那么目前最大收益将为当前屋子的价值加上上一间屋子选择不偷时的最大收益。而如果选择不偷，则对于上一间房子来说，可以偷，也可以不偷，当前的最大收益为 max(偷上一间房子达到的最大收益，不偷上一间房子达到的最大收益) 。可以得出以下公式：
```
max_steal = max_not_steal + houses[i]
max_not_steal = max(max_steal, max_not_steal)
```

根据上面的公式，进行计算即可得到答案。