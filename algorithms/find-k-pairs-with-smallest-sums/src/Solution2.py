import heapq


class Solution:
    def kSmallestPairs(self, nums1: 'List[int]', nums2: 'List[int]',
                       k: 'int') -> 'List[List[int]]':
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        heap = [(nums1[0] + nums2[i], 0, i) for i in range(len(nums2))]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            if heap:
                res, i, j = heapq.heappop(heap)
                ans.append([nums1[i], nums2[j]])
                if i + 1 < len(nums1):
                    heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        return ans
