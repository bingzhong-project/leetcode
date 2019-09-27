class Solution:
    def maxChunksToSorted(self, arr: list) -> int:
        res = 0
        cur = 0
        i = 0
        while i < len(arr):
            cur = arr[i]
            j = i + 1
            while j < cur + 1:
                cur = max(cur, arr[j])
                if cur == len(arr) - 1:
                    return res + 1
                j += 1
            i = j
            res += 1

        return res
