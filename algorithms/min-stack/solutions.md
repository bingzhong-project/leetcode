# Min Stack

[问题描述](https://leetcode.com/problems/min-stack/)

## 知识点

栈，代码设计

## 解题思路

设计的关键在于如何维护栈的最小值以及在常量时间内获取栈的最小值。有下面两种解法。

### 解法一

栈的实现通常就是维护一个列表，由于还有最小值的管理，可以再定义多一个域用于保存最小值，在获取最小值时直接返回这个最小值域即可。  
而当栈发生变化时，最小值也可能会发生变化，即 push 或 pop 方法被调用。push 方法被调用就是简单的将当前最小值与传递进来的 x 值作比较，保留更小的值即可。当调用 pop 方法时，就需要判断出栈的是否为最小值，如果是就需要遍历列表，重新找出最小值。  
这种方法在正常使用时是没有问题的，毕竟出栈时刚好是最小值的情况并不多，但是如果将一个排好序的数组以从大到小的方式入栈，然后再一直出栈元素时，pop 方法将会表现得非常差。

### 解法二

另一种解法是在执行 push 操作时，将 x 与当前栈中的最小值作比较，然后将 x 与最小值组成新的元素并入栈。当出栈时，直接将元素出栈即可，而当访问栈中最小值时，返回栈顶元素所存储的最小值即可。

这是利用了栈后进先出的特性。我们可以将第 n 个元素入栈时，将栈的状态标记为 A ，而第 n + 1 个元素入栈时，栈的状态为 B ，当发生出栈行为时，栈的状态就会从 B 变回之前的 A 。所以当栈中有 n 个元素，而第 n + 1 个元素入栈时，第 n + 1 个元素并不会影响到 1..n 元素集合的最小值。