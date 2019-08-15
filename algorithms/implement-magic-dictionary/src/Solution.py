import collections


class MagicDictionary:
    def buildDict(self, dict: 'List[str]') -> 'None':
        """
        Build a dictionary through a list of words
        """
        self.single = set()
        self.dict = collections.defaultdict(list)
        for s in dict:
            if len(s) == 1:
                self.single.add(s)
            else:
                self.dict[s[0]] += [s]
                self.dict[s[-1]] += [s]

    def search(self, word: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        if len(word) == 0:
            return False
        if len(word) == 1:
            if self.single and word not in self.single:
                return True
            else:
                return len(self.single) > 1
        if word[0] in self.dict:
            for dict in self.dict[word[0]]:
                if len(word) != len(dict):
                    continue
                diff = 0
                for i in range(len(word)):
                    if word[i] != dict[i]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    return True
        if word[-1] in self.dict:
            for dict in self.dict[word[-1]]:
                if len(word) != len(dict):
                    continue
                diff = 0
                for i in range(len(word)):
                    if word[i] != dict[i]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    return True
        else:
            return False
        return False
