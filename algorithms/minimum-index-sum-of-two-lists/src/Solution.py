class Solution:
    def findRestaurant(self, list1: 'List[str]',
                       list2: 'List[str]') -> 'List[str]':
        pos1 = {}
        pos2 = {}
        words = set()
        for i in range(len(list1)):
            word = list1[i]
            pos1[word] = i
            words.add(word)
        for i in range(len(list2)):
            word = list2[i]
            pos2[word] = i
            words.add(word)
        res = []
        index = 2**31
        for word in words:
            if word in pos1 and word in pos2:
                temp_index = pos1[word] + pos2[word]
                if temp_index < index:
                    res = [word]
                    index = temp_index
                elif temp_index == index:
                    res.append(word)
        return res
