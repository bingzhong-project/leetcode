# [Pyramid Transition Matrix](https://leetcode.com/problems/pyramid-transition-matrix/)

## 解题思路

首先根据给出的 allowed 构建出基层可以搭建的字符映射集合。

如例子：bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]

那么可以得到以下集合：

```python
data['BC'] = G
data['CD'] = E
data['GE'] = A
data['FF'] = F

```

然后从底层一层层的往上遍历，每遍历到一层，根据当前所在的基层字符，构建上面一层的字符。  
当当前层次长度为 2 而上一层次长度为 1 ，表示已经搭到顶层，成功。  
而当当前层次长度和上一层层次长度相差 1 ，表示当前层的上一层已经搭建完成，递归，以同样的方法处理。
