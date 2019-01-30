class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def get_next_words(word, wordList):
            words = []
            for i in range(len(word)):
                left, right = word[:i], word[i + 1:]
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == char:
                        continue
                    next_word = left + char + right
                    if next_word in wordList:
                        words.append(left + char + right)

            return words

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = []
        queue.append(beginWord)
        layer = 1

        while len(queue) > 0:
            layer += 1
            for _ in range(len(queue)):
                word = queue.pop(0)
                for next_word in get_next_words(word, wordList):
                    if next_word == endWord:
                        return layer
                    queue.append(next_word)
                    wordList.remove(next_word)

        return 0
