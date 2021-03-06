# Reorder List

[问题描述](https://leetcode.com/problems/reorder-list/)

## 知识点

快慢指针，链表反转，链表合并

## 解题思路

解题的思路为将链表以中间节点一分为二，然后将后半的链表反转，之后就是两个链表合并，将后半链表的元素插入到前半链表的间隔。  
有以下示例：

```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

分割链表：

```
1 -> 2 -> 3
4 -> 5 -> 6
```

后半链表反转：

```
1 -> 2 -> 3
6 -> 5 -> 4
```

之后两个链表合并：

```
1  ->  2  ->  3
   6   ->  5  ->  4
```

最后得出结果：

```
1 -> 6 -> 2 -> 5 -> 3 -> 4
```

实际操作的思路有两种。

### 思路 1

遍历一遍链表，将链表存进一个列表中。这样将列表从尾遍历到头，就相当于获取到了经过反转处理的后半链表，之后进行链表合并即可。  
但是这种思路需要 O(n) 的空间复杂度。

### 思路 2

其实上述提到的三种链表操作，寻找中间点分离链表，反转链表，合并链表都可以在常量空间完成。  
通过快慢指针寻找链表的中间节点，之后根据该中间节点分离链表。  
而反转链表通过永远指向链表头的 dummy 节点完成。  
最后合并链表的操作也很简单，分别遍历两个链表即可完成。
