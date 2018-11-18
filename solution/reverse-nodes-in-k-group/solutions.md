> [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)

# 知识点
反转单链表

# 解题思路
解题思路为分解链表，然后局部反转链表。  
反转链表的做法为，设置一个 dummy 节点，即假节点，永远指向链表的首节点，还有一个 last 指针，一直指向未进行反转前的链表的首节点，因为原先链表的首节点将会变成末尾节点。以而下链表为例。  
```
1 -> 2 -> 3 -> 4 -> 5
```
声明一个 dummy 节点，节点值为 -1 ，next 指针指向 1 节点，如下：
```
-1 -> 1 -> 2 -> 3 -> 4 -> 5
      ⬆
     last
```
然后上面提到的 last 指针，将会一直指向 1 节点。  

last 指针指向的节点称为 last 节点，其 next 指针指向的节点称之为 next_node 节点。  
不断进行以下操作，让 dummy 节点的 next 指针指向 next_node 节点，然后 last 节点的 next 指针指向 next_node 节点的 next 节点，label_next 节点的 next 指针指向 last 节点，直到 last 的 next 节点为空。以上面的链表为例，第一次循环后的链表为：
```
-1 -> 2 -> 1 -> 3 -> 4 -> 5
           ⬆
          last
```
然后第二次循环将会是：
```
-1 -> 3 -> 2 -> 1 -> 4 -> 5
                ⬆
               last
```
然后整个链表将会完成反转：
```
-1 -> 5 -> 4 -> 3 -> 2 -> 1
                          ⬆
                         last
```
dummy 节点的 next 指针就指向了完成反转的链表的头节点。可以参考以下反转链表的代码
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(head):
    dummy = ListNode(-1)
    dummy.next = head
    last = dummy.next
    while last.next is not None:
        next_node = last.next
        last.next = next_node.next
        next_node.next = dummy.next
        dummy.next = next_node
    return dummy.next

```

上面为反转链表的知识，而题目需要做到的是局部反转链表。  
局部反转链表的话，那么首先就是分解链表，用 start 来指向局部链表的头节点的前一个节点，用 end 来指向局部链表的尾节点的下一个节点，当然要 end 指针赋值成功，需要边计数边遍历链表。以 k=2 ，即将链表以两个元素为一个局部链表为例。如下：
```
    -1 -> 1 -> 2 -> 3 -> 4 -> 5
     ⬆              ⬆
   start           end
```
那么在开始，其实 start 指向的就是 dummy 节点。开始进行局部链表反转，反转结束的标志不再是 last 节点的 next 指针是否为空，而是 last 指针的 next 指针是否指向了 end 。当局部链表反转完成后，局部链表的头尾指针将成为下一轮局部遍历的 start 指针。
```
    -1 -> 1 -> 2 -> 3 -> 4 -> 5
               ⬆              ⬆
             start           end
```
当 end 指针为空，即表示全部反转完毕。