# [My Calendar II](https://leetcode.com/problems/my-calendar-ii/)

## 知识点

有序字典

## 解题思路

利用有序字典 TreeMap 以以下方式方式存储数据：

```java
treeMap.put(start, 1);
treeMap.put(end, -1);
```

遍历 treeMap 并计数，遍历 treeMap 是有序的，即会先拿到靠前的日期值。  
如果计数等于 0 ，即没有重合，刚好一个日期区间，如果计数大于 2 开始，就证明有日期重合了，由于题目允许重合，即当计数大于等于 3 时，才无法添加日期。
