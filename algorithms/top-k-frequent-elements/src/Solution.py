class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        table = {}
        for n in nums:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1
        heap = [(2**-31, 2**31) for _ in range(k)]
        for key, val in table.items():
            frequent, num = heap[0]
            if frequent < val:
                heap[0] = (val, key)
                self.heapify(heap)

        return [n for _, n in heap]

    def heapify(self, heap, i=0):
        hsize = len(heap)
        left = 2 * i + 1
        right = 2 * i + 2
        minimum = i
        if left < hsize and heap[left] < heap[minimum]:
            minimum = left
        if right < hsize and heap[right] < heap[minimum]:
            minimum = right
        if minimum != i:
            temp = heap[minimum]
            heap[minimum] = heap[i]
            heap[i] = temp
            self.heapify(heap, minimum)
