class Solution:
    def replaceWords(self, dict: 'List[str]', sentence: 'str') -> 'str':
        sentence = sentence.split(' ')
        dict.sort(key=lambda x: len(x))
        for i in range(len(sentence)):
            for d in dict:
                if sentence[i].startswith(d):
                    sentence[i] = d
        return " ".join(sentence)


if __name__ == "__main__":
    print(Solution().replaceWords(["cat", "bat", "rat"],
                                  "the cattle was rattled by the battery"))
