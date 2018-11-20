> [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

# 知识点
动态规划

# 解题思路
使用动态规划进行解题。对于第 i 位数来说，其最大子数组和有可能是前面位数组成的子数组和加上自身，又或者自身即是最大子数组和。  
声明一个数组 max_cache ，max_cache[i] 标识当遍历到第 i 位时，最大的子数组和。有公式：
```
               max_cache[i] = nums[i] if i == 0
max_cache[i] = 
               max(max_cache[i - 1] + nums[i], nums[i]) if i > 0
```

根据上面的公式可以发现，对于数组 max_cache ，用到的总是上一个位置的值，即 max_cache[i - 1] ，所以可以进行优化，只利用 max_cache 记忆上一位的最大子数组和即可。  
```
               max_cache = nums[i] if i == 0
max_cache = 
               max(max_cache + nums[i], nums[i]) if i > 0
```

之后根据上面的公式进行计算即可。

TODO: 使用分治法进行解题