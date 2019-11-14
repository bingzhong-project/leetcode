class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        ans = {}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                ans[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        res = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            if nums1[i] in ans:
                res[i] = ans[nums1[i]]

        return res
