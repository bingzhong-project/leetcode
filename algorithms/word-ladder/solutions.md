# Word Ladder

[问题描述](https://leetcode.com/problems/word-ladder/)

## 知识点

广度优先搜索

## 解题思路

可以将问题转化为，由从英文字符组成的 word 构建成的一颗树中，找出 beginWord 到 endWord 的距离。而解决这类问题，可以利用广度优先搜索计算出结点之间的距离。  
首先要注意的是 word 的变换规则，将变换规则作为 word 与 word 之间是否存在路径的依据，则如果指定 word A 通过变换规则可以变换为 word B ，则表示 word A 与 word B 之间存在路径。而在本题中，还多了一个规则，那就是变换得到的词是否在 wordList 中。之后就是通过广度优先搜索计算结点距离。由于求的是给定 beginWord 到某个指定结点的距离，所以不用记录下所有结点的距离，在广度优先搜索中计算层数即可，当 beginWord 变换成 endWord 时，当前层数即为答案。
