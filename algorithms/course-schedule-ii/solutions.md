# Course Schedule II

[问题描述](https://leetcode.com/problems/course-schedule-ii/)

## 知识点

深度优先搜索，拓扑排序

## 解题思路

解题思路为利用深度优先搜索进行拓扑排序。思路和 [Course Schedule Solution](https://gitee.com/bingzhong-project/leetcode/blob/master/algorithms/course-schedule/solutions.md) 一致。

在拓扑排序中，越晚完成遍历的节点越靠近表头。基于这样的思路，当节点完成深度优先搜索后就插入到列表的表头（实际做法中可以加入到表尾，最后再反转数组）。
