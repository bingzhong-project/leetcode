import heapq


class Solution:
    def kSmallestPairs(self, nums1: 'List[int]', nums2: 'List[int]',
                       k: 'int') -> 'List[List[int]]':
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            if heap:
                res, i, j = heapq.heappop(heap)
                ans.append([nums1[i], nums2[j]])
                if j + 1 < len(nums2):
                    heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
