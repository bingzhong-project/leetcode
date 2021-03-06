# Rotate List

[问题描述](https://leetcode.com/problems/rotate-list/description/)

## 知识点

旋转链表

## 解题思路

旋转链表与反转链表一样，需要一个 dummy 节点，dummy 节点的 next 指针一直指向链表的头节点。  
然后需要做得是，如何找出旋转节点，旋转节点，也是链表旋转后的尾节点。对题目分析，不难得出，旋转节点为第 n = length - k % length 个节点，当 n 为 0 时，指的是 dummy 节点，将不需要旋转，而 n 等于 length 时，表示原链表的尾节点为旋转点，因为旋转节点将成为尾节点，原来就是尾节点将表示不用旋转，在这两种情况下，直接返回原链表即可。  
如果不是上述得两种情况，就需要进行链表的旋转。有以下链表：

```
1 -> 2 -> 3 -> 4 -> 5
```

当 k = 2 时，n = length - k % length 为 3 ，即第 3 个节点为旋转节点。

```
-1 -> 1 -> 2 -> 3 -> 4 -> 5
                ⬆
             rotate
```

接下来，dummy 节点的 next 指针将指向旋转节点的 next 节点。rotate 的 next 指针将变为空，因为旋转节点将成为新的尾节点。这样做的话，原链表将会分裂成两个链表。

```
1 -> 2 -> 3
-1 -> 4 -> 5
```

现在面临的问题是，如何将分裂除的两条链表连起来。可以观察到，当链表进行反转后，原链表的尾节点将和原链表的头节点连接起来。所以在开始反转前，先找出头节点和尾节点，分别用 head 指针和 tail 指针标记，当链表开始进行旋转，分裂成两条链表后，再将原链表的首尾节点连接起来就完成了链表的旋转。完成旋转后，返回 dummy 的 next 节点既可，因为 dummy 节点的 next 指针一直指向链表的首节点。
