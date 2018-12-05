> [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

# 知识点
动态规划

# 解题思路
先查看 target 为 1 ~ 4 的组合和结果。
```python
if target == 1:
    result = [
        (1)
    ]
elif target == 2:
    result = [
        (1, 1), 
        (2)
    ]
elif target == 3:
    result = [
        (1, 1, 1), 
        (1, 2), 
        (2, 1),
        (3)
    ]
elif target == 4:
    result = [
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
    ]
```

观察上述的结果，有这样的规律：存在 num 为给定数组 nums 中的元素，当 target >= num 时，数 num 与数 (target - num) 的组合和元素分别组合将得到满足和为 target 的组合和，该组合和的元素个数和数 (target - num) 的组合和的个数一样。  
举个例子，[1, 2, 3] 和 4 ，首先有 num = 1 ，那么 target - num 为 3 。3 的组合和结果为：
```
(1, 1, 1), 
(1, 2), 
(2, 1),
(3)
```

这时和 1 进行组合：
```
(1) + (1, 1, 1) = (1, 1, 1, 1)
(1) + (1, 2) = (1, 1, 2)
(1) + (2, 1) = (1, 2, 1)
(1) + (3) = (1, 3)
```

之后继续遍历 nums ，延续这种处理，将会得到和为 4 的组合和。组合和的数量为：4 + 2 + 1 = 7 。  

了解到这个后，定义数组 dp ，dp[i] 为当 target 为 i 时的组合和元素数量。转移有以下状态方程
```
        1 if i == 0 # 当 i 为 0 时，表示自身即可形成组合和，所以元素个数为 1
dp[i] = 
        dp[i] + dp[num - i] if i >= num
```