class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(m, n, index, board, word, path=""):
            if m < 0 or n < 0 or m >= len(board) or n >= len(
                    board[0]) or index == len(
                        word) or board[m][n] != word[index]:
                return False
            path += board[m][n]
            if len(word) == len(path):
                return True
            board[m][n] = chr(ord(board[m][n]) ^ 128)
            is_exist = dfs(m - 1, n, index + 1, board, word, path) or dfs(
                m + 1, n, index + 1, board, word, path) or dfs(
                    m, n - 1, index + 1, board, word, path) or dfs(
                        m, n + 1, index + 1, board, word, path)
            board[m][n] = chr(ord(board[m][n]) ^ 128)
            return is_exist

        for n in range(len(board[0])):
            for m in range(len(board)):
                is_exist = dfs(m, n, 0, board, word)
                if is_exist:
                    return is_exist
        return False
