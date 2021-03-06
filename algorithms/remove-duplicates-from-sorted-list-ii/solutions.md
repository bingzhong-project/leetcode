# Remove Duplicates from Sorted List II

[问题描述](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

## 知识点

链表

## 解题思路

本题需要删除所有重复的节点，而链表的节点使有序的，那么重复的节点也是连续的，可以使用一个 start 指针指向需要删除的子链表的前一个节点，以及用一个 end 指针指向一个需要删除的子链表的后一个节点。  
这里需要注意，对链表进行删除操作，可能会丢失掉头节点，所以再开始前需要声明一个 dummy 链表节点，值为 -1 ，next 指针一直指向链表的头节点，这样就不会丢失头节点，并且可以更加平滑的处理整个删除重复节点的流程。  
假设有以下链表：

```
1 2 3 3 4 4 5
```

那么开始处理时，将如下：

```
 -1 1 2 3 3 4 4 5
  ⬆
start
```

现在开始寻找 end 指针需要指向的节点。首先获取 start 指针的下一个节点 node ，根据上面的例子就是 1 节点，end 指针将指向 1 节点的下一个节点，即 2 节点。然后判断这两个节点的值是否相等，如果相等，拿就重复上面的过程，直到 node 和 end 的值不相等。这个过程是需要计数的，计算重复了多少次以上步骤，用于判断是否发现了重复节点。

```
 -1  1  2  3  3  4  4  5
  ⬆     ⬆
start  end
```

没有发现重复节点，那么 start 指针将指针当前 start 节点的下一个节点。

```
 -1  1  2  3  3  4  4  5
     ⬆
   start
```

再进行上面的步骤，也是没有重复节点，所以 start 指针将指向 2 节点。

```
 -1  1  2  3  3  4  4  5
        ⬆
      start
```

接下来再次重复上面的步骤。

```
 -1  1  2  3  3  4  4  5
        ⬆        ⬆
      start     end
```

这次发现了重复节点，将 start 以及 end 之间的子链表删除。

```
 -1  1  2  4  4  5
        ⬆
      start
```

这时 start 指针保留原样，然后再重复上述的步骤，直到 start 指针为空，链表将会删除掉所有的重复节点。
