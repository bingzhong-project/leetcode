class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        def heapify(heap, i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(heap) and heap[left] > heap[largest]:
                largest = left
            if right < len(heap) and heap[right] > heap[largest]:
                largest = right
            if i != largest:
                temp = heap[i]
                heap[i] = heap[largest]
                heap[largest] = temp
                heapify(heap, largest)

        def add_heap(heap):
            i = len(heap) - 1
            p = i // 2 - 1 if i % 2 == 0 else i // 2
            while i > 0 and heap[p] < heap[i]:
                temp = heap[i]
                heap[i] = heap[p]
                heap[p] = temp
                i = p
                p = i // 2 - 1 if i % 2 == 0 else i // 2

        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(heap) < k:
                    heap.append(matrix[i][j])
                    add_heap(heap)
                elif heap[0] > matrix[i][j]:
                    heap[0] = matrix[i][j]
                    heapify(heap, 0)

        return heap[0]
