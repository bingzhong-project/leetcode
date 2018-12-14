# Partition List

[问题描述](https://leetcode.com/problems/partition-list/description/)

## 知识点

链表，指针

## 解题思路

使用两个指针 front 和 back ，分别指向前后紧挨的两个节点。  
在开始前，构建一个假节点 dummy ，其 next 指针一直指向链表的头节点。

```
 -1     1     4     3     2     5     2
  ⬆     ⬆
front back
```

然后，front 和 back 指针同时向前移动，直到 back 指针指向的值大于等于给定值 x 。

```
 -1     1     4     3     2     5     2
        ⬆     ⬆
      front back
```

之后，再引入一个指针 insert ，用于标记节点每次插入到前面的插入点。开始时，insert 指针与 front 指针指向同一个节点。

```
 -1     1     4     3     2     5     2
        ⬆     ⬆
      front back
      insert
```

之后 front 和 back 指针继续向前移动，当 back 指向的节点的值小于 x 时，发生节点的移动。这时就是简单的链表指针操作，原 front 指针指向 back 的下一个节点，而原先 back 节点则插入到 insert 处。然后 back 指针指向 front 的下一个节点，而 insert 指针则向前一步，标记下一次的插入点。  
下面为链表发生第一次变化后的状态：

```
 -1     1     2     3     4     5     2
              ⬆     ⬆     ⬆
            insert front back
```

重复上面的过程，直到 back 指针遇到边界，则完成链表的分区。
