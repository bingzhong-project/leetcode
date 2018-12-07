> [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

# 知识点
深度优先搜索

# 解题思路
总体的解题思路和 [Populating Next Right Pointers in Each Node](https://gitee.com/bingzhong-project/leetcode/blob/master/algorithms/populating-next-right-pointers-in-each-node/solutions.md) 相似，通过深度优先搜索遍历树和通过已经构建好的 next 指针进行同层访问。  
在本题中，会有残缺节点的出现，必须遍历同层节点，直到找到合适的 next 节点。   
但是需要注意，如果在遍历时，水平方向上的遍历是从左到右的话，可能会由于残缺节点而无法通过 next 指针找到同层节点，因为从左到右的遍历，会先处理好左子树，然后才会处理右子树，而在左子树的处理期间，右子树是没有构建好 next 指针的。  
所以这时需要反过来，从右往左遍历，这样就保证到每次处理时，涉及到的节点的 next 指针已经处理完成，可以通过其找到同层节点。