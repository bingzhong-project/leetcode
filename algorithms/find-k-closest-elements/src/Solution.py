class Solution:
    def findClosestElements(self, arr: 'List[int]', k: 'int',
                            x: 'int') -> 'List[int]':
        arr.sort()
        left = 0
        right = len(arr) - 1
        index = None
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] < x:
                left = mid
            elif arr[mid] > x:
                right = mid
            else:
                index = mid
                break
        if index is None:
            index = left if abs(arr[left] - x) < abs(arr[right] - x) else right

        res = []
        left = index
        right = index + 1
        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right > len(arr) - 1:
                res.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1

        return sorted(res)
