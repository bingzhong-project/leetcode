class Solution:
    def reverseWords(self, s: 'str') -> 'str':
        def reverse(string):
            string = list(string)
            left = 0
            right = len(string) - 1
            while left < right:
                temp = string[left]
                string[left] = string[right]
                string[right] = temp
                left += 1
                right -= 1
            return "".join(string)

        sub_string = s.split(' ')
        res = []
        for string in sub_string:
            res.append(reverse(string))

        return ' '.join(res)
