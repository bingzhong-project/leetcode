> [House Robber II](https://leetcode.com/problems/house-robber-ii/description/)

# 知识点
动态规划

# 解题思路
总体的解题思路与 [House Robber 解题思路](https://gitee.com/bingzhong-project/leetcode/blob/master/solution/house-robber/solutions.md) 相同。  
不同的是，本题中给出的数组为环形，即首尾相连。由于首尾相连，所以首尾是互斥的，偷第一间房子，即不可以偷最后一间房子，反之亦然。  
转换一下思路，由于首尾互斥，可以假设永远不偷最后一间屋子，第一间房子就可以选择偷与不偷，不受限制，求出 1..n-1 的最大收益。然后假设永远不偷第一间房子，求出 2..n 的最大收益，最后将这两个结果进行比较，较大值者即为结果。  