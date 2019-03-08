# Largest Number

[问题描述](https://leetcode.com/problems/largest-number/)

## 知识点

排序

## 解题思路

问题的核心在于如何排序出最大序列组合，那么问题就变成如何比较各个元素的大小。假如有 3 和 30 ，330 比 303 大，即认为元素 3 比元素 30 大，所以 3 排在 30 前，即排序的大小比较方法为：

```python
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

```

按照上述的排序方法对给定数组进行排序，得到的就为结果。
