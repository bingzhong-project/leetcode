class Solution:
    def kSmallestPairs(self, nums1: 'List[int]', nums2: 'List[int]',
                       k: 'int') -> 'List[List[int]]':
        def heapify(heap, i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(heap) and heap[left] > heap[largest]:
                largest = left
            if right < len(heap) and heap[right] > heap[largest]:
                largest = right
            temp = heap[i]
            heap[i] = heap[largest]
            heap[largest] = temp
            heapify(heap, largest)

        heap = [None for _ in range(k)]
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            pass
