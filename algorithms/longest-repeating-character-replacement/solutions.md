# [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

## 知识点

滑动窗口

## 解题思路

### 思路 1

思路 1 属于暴力破解。对给定字符串进行迭代，然后逐个字符串的计算出可替换的最长重复字符串。算法复杂度介于 O(kn) 到 O(n²) 。

### 思路 2

思路 2 为利用滑动窗口的思想。字符串的滑动窗口思想核心为**根据窗口的变化、移动来实时进行字符计数**。  
窗口的初始大小为 k ，因为在 k < len(s) 的情况下，可替换的最长重复字符串最小肯定为 k 。利用指针 left 和 right 来标记窗口，left 为窗口左边界，right 为有边界，结合题目，left 的初始值为 0 ，而 right 为 k 。声明一个字典 counter 对窗口内的字符进行计数。  
之后开始移动窗口，右边界向右扩展，对字符进行计数。如果这时窗口长度 length 大于出现最多次数的字符的数量 max_count ，并且 length - max_count > k ，则表示该窗口内的字符串无法构成最长字符串，这时需要让左边界收缩，同时更新窗口字符计数。如果符合的要求的话，即计下窗口长度。最终最大的窗口长度即为答案。
