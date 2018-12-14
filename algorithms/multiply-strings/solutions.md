# Multiply Strings

[问题描述](https://leetcode.com/problems/multiply-strings/)

## 知识点

错位相乘

## 解题思路

解题思路主要是利用错位相乘的思路。  
以 289\*785 为例：  
![错位相乘示例图](https://bingzhong-project.gitee.io/public/pictures/错位相乘示例图.png)

将 num1 和 num2 拆成一位一位数的相乘计算，将结果缓存起来，后续进行相加并控制进位即可。注意当进行到最后一位的相加阶段时的进位处理。而根据错位相乘的规则，用于缓存 num1 和 num2 逐位相乘结果的数组为：

```python
cache = [
        [0 for _ in range(len(num1) + len(num2) - 1)]
        for _ in range(len(num2))
        ]
```
