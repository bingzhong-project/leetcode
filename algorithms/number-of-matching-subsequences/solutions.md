# [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)

## 知识点

数组，字典

## 解题思路

参考资料：[Number of Matching Subsequences Solution](https://www.cnblogs.com/grandyang/p/9201323.html)

一种暴力解题的思路为对每个遇到的 word ，与 S 比较检查是否为子序列字符串。但是在遇到大字符串时将 TLE 。

另一种思路为利用字典作为备忘录 memo ，记录当前遍历到的每个 word 的单字符位置。利用 memo 记录当前遍历到的各个 word 的位置。  
遍历 words ，以元组的形式记录下 (word 所在 words 中的索引，word[i] 的下一个字符索引)

以题目示例为例子：

```text
S = "abcde"
words = ["a", "bb", "acd", "ace"]
```

开始时，所有 words 中的字符都会从第一个字符开始遍历，所以有：

```python
memo['a'] = [(0, 1), (2, 1), (3, 1)]
memo['b'] = [(1, 1)]
```

然后开始遍历 S 。第一个遇到的字符为 a ，那么 memo 的变化如下：

```python
memo['c'] = [(2, 2), (3, 2)]
memo['b'] = [(1, 1)]
```

由于 words[0] 只有一个字符 a ，所以没有下一个字符了，表明改字符串是 S 的子序列字符串。

接下来遍历到 b ，有：

```python
memo['c'] = [(2, 2), (3, 2)]
memo['b'] = [(1, 2)]
```

然后到 c ，有：

```python
memo['d'] = [(2, 3)]
memo['e'] = [(3, 3)]
memo['b'] = [(1, 2)]
```

之后到 d ，有：

```python
memo['e'] = [(3, 3)]
memo['b'] = [(1, 2)]
```

由于 words[2] 最后一个为 d ，已经遍历完成，表明为 S 的子序列子串。

最有到 e ，有：

```python
memo['b'] = [(1, 2)]
```

words[3] 最有一个字符为 e ，没有下一个了，禀明为 S 的子序列子串。

最后得出了子序列字串的结果数量。
