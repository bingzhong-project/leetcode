# [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

## 知识点

字符串，回文字

## 解题思路

根据回文字的特性，有 i = 0 ，j = len(s) - 1 ，这时如果 s[i] == s[j] ，那么 s 是否为回文字取决于 s[i + 1:j] 是否为回文字。  
根据上面提及的回文字特性，从字符串的开头与结尾遍历字符串，如果遇到 s[i] != s[j] ，那么该字符不是回文字，但是题目允许删除一个字符，这是需要考虑的是删除 s[i] 字符还是 s[j] 字符使得删除后的字符串为回文字。  
这时就需要分别判断 s[i + 1:j + 1] 以及 s[i:j] 子串的其中一个是否为回文字，如果是，那么给定的字符串即符合题目要求。