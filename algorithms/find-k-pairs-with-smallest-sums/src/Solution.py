class Solution:
    def kSmallestPairs(self, nums1: 'List[int]', nums2: 'List[int]',
                       k: 'int') -> 'List[List[int]]':
        def heapify(heap, hsize, i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < hsize and sum(heap[left]) > sum(heap[largest]):
                largest = left
            if right < hsize and sum(heap[right]) > sum(heap[largest]):
                largest = right
            if i != largest:
                temp = heap[i]
                heap[i] = heap[largest]
                heap[largest] = temp
                heapify(heap, hsize, largest)

        def build_heap(heap, hsize):
            for i in range(hsize // 2, -1, -1):
                heapify(heap, hsize, i)

        if len(nums1) == 0 or len(nums2) == 0:
            return []

        heap = []
        hsize = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair = (nums1[i], nums2[j])
                if hsize < k:
                    heap.append(pair)
                    hsize += 1
                    build_heap(heap, hsize)
                elif sum(pair) < sum(heap[0]):
                    heap[0] = pair
                    heapify(heap, hsize, 0)

        return [list(pair) for pair in heap]
