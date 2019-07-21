# [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

## 知识点

贪心算法

## 解题思路

### 思路 1

思路 1 参考：[Task Scheduler Solution](https://www.cnblogs.com/grandyang/p/7098764.html)

### 思路 2

思路 2 为先找出出现最高频率的任务，若任务列表中只有该任务，则需要等待的空闲数为：

```text
idle = n * (max_frequency) - 1
```

按照题目给出的例子，则任务调度为：

```text
A idle idle A idle idle A
```

而当任务列表中部只含有最高频率的任务，则可以将其他任务安插在 idle 的位置上，即需要等待的空闲数能够减少。

如果要安插的任务的频率少于最大频率，则当前空闲数直接减去该任务的频率即可。如果像题目一样，A 和 B 的出现频率是一样的，都为最大频率，这时就不可以直接减去 B 的频率，而是减去 (B_frequency - 1) ，因为 B 的频率和 A 一样，最后一个任务将会安排到最后，本身就没有空闲需要等待。
