# Beautiful Arrangement

[问题描述](https://leetcode.com/problems/beautiful-arrangement/)

## 知识点

回溯，动态规划

## 解题思路

一种简单的解决思路是直接利用回溯法，利用题目给出的要求作为回溯条件，然后记录统计数量即可。  
但是直接利用回溯法的话，会遍历访问许多分支，进行了多次重复计算，从而降低了整体的速度。  
为了解决这个问题，可以在回溯的基础上加上动态规划的思路。这里利用自顶向下的解题思路，同时记录下已经计算出的结果，从而避免重复计算。  
一下分别为 N = 2 和 N = 3 时构建出的树：

![beautiful-arrangement-2](https://bingzhong-project.gitee.io/public/pictures/beautiful-arrangement-2.png)  
![beautiful-arrangement-3](https://bingzhong-project.gitee.io/public/pictures/beautiful-arrangement-3.png)

可以看到在 N = 3 的树包含了 N = 2 构建的树，也就是如果直接使用回溯，就会重复计算了 N = 2 。

可以将问题描述成这样，对于给定数字 N 来说，当有 i = N 个位置待排，而待构造的数组为 numbers （ numbers 的初始值为 1 到 N 的数组） 时，可以构造的优雅排列的数量是多少。  
声明一个字典 dp ，而元组 (i, numbers) 作为 key ，记录当有 i 个位置待排，且待构造的数组为 numbers 可以构造出多少个优雅排列。在遍历树时，通过判断 dp 中是否记录了已经计算了的结果，从而避免重复计算。
