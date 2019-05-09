# [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## 知识点

深度优先搜索，广度优先搜索

## 解题思路

比较典型的对图进行遍历，找出符合要求的结点。  
直观的做法是对所有结点都进行搜索，然后判断是否要求，但是这样的做法只能刚好 AC 。  
优化的方法为一种逆向思维。符合要求的结点时能够在指定条件下到达给定数组的边界，那么只从边界结点开始进行遍历，逆向条件找出能够到达的结点。
