class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        def heapify(array, hsize, i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < hsize and array[left] > array[largest]:
                largest = left
            if right < hsize and array[right] > array[largest]:
                largest = right
            if largest != i:
                tmp = array[i]
                array[i] = array[largest]
                array[largest] = tmp
                heapify(array, hsize, largest)

        def build_max_heap(array):
            for i in range(len(array) // 2, -1, -1):
                heapify(array, len(array), i)

        def remove_max(array, hsize):
            max = array[0]
            array[0] = array[hsize - 1]
            heapify(array, hsize - 1, 0)
            return max

        build_max_heap(nums)
        hsize = len(nums)
        res = None
        for i in range(k):
            res = remove_max(nums, hsize)
            hsize -= 1

        return res
