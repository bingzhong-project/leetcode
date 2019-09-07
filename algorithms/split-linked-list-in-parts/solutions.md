# [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)

## 知识点

链表

## 解题思路

题目的难点在于如何确定划分出的各个子链表的长度。  
首先先遍历一遍链表，计算出链表的长度 size ，然后用 size 除 k ，得到结果 div 以及余数 mod ，然后再声明一个长度为 k 的数组 split_sizes ，用于存储的是各个子链表的长度，当 size 除 k 除不尽时，有链表的长度会多 1 ，且规定了左边的子链表 >= 右边的子链表，所以计算子链表长度 split_size 的公式如下：

```text
             div if mod == 0
split_size =
             div + 1 if mod > 0 then mod -1
```

得知各个子链表长度后，就是根据长度来分离链表。
