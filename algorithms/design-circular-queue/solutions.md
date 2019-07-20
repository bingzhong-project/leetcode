# [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

## 知识点

循环队列

## 解题思路

循环队列时一个线性列表，当队头或是队尾到达列表尾时，将会回到列表头。  
列表打大小为 size = k + 1 ，k 为队列长度。  
队列为空的判断为 head == tail ，而队列为满的判断为 head == (tail + 1) % size 。
