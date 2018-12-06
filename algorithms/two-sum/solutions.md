> [Two Sum](https://leetcode.com/problems/two-sum/description/)

# 知识点
哈希表

# 解题思路
求两数之和数的和是否为目标数，可以利用减法。设目标数为 S ，会有：  
```math
S - x - y = 0
```
每次让目标数减去指定数，得到的结果就是新的目标数，然后只要找出和新目标数相等的数，就可以得到能够相加等于目标数的两个数字。  

接下来就简单了，只要用目标数减去指定数，得出差值，然后再从给定数组中查找是否存在与该差值相等的数即可。  
但是这样的话，需要两个循环，外层循环求每个数的差，内存循环判断差知否存在于给定数组中。这样的话时间复杂度为 O(n<sup>2</sup>) 。  
两层循环存在的原因在于，在数组中查找是否存在一个数需要进行遍历，当然数组有序的话可以利用二分查找。但是有更好的方案，就是利用哈希表，哈希表的查找指定的 Key 是否存在的时间复杂度为 O(1) ，将数组中的数缓存到哈希表中，Key 为数组中的各个数，Value 为数组下标，这样就可以快速找到能够相加等于目标值的两个数在数组中的下标。  