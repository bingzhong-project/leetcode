# [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

## 知识点

栈

## 解题思路

参考：[Score of Parentheses Solution](https://www.cnblogs.com/grandyang/p/10634116.html)

分析题目，对于分数的计算，有以下的规则：

1. 整体的分数计算其实可以化为一条计算式子去计算。
2. 遇到 "(" 表示一个新值的计算开始，可以理解为式子中括号内的计算开始。
3. 遇到 ")" 表示开始计算括号内值的结果

声明一个变量，用于记忆当前计算式子括号内的临时结果。遍历括号字符串，遇到 "(" 很简单，表明局部计算开始，将当前的计算结果存起来，然后重置当前的计算结果。  
遇到 ")" 则有两种可能，一种是遇到了 "()" ，那么当前临时结果为 1 ，而遇到的是 "(())" 这种形式，则有可能需要进行乘 2 处理，这个是否乘 2 则是由是否已经计算了内部括号的值，即当前临时结果是否 > 0 。  
之后在遍历中，逐个的将计算结果相加起来即可。
