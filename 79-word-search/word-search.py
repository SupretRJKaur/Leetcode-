class Solution:

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ch = board[i][j]
                    board[i][j] = "0"
                    if self.isExist(board, word, i, j, 0):
                        return True
                    board[i][j] = ch
        return False

    def isExist(self, board, word, r, c, idx):
        if idx == len(word) - 1:
            return True

        up = False
        down = False
        left = False
        right = False

        if (
            r > 0
            and idx < len(word) - 1
            and board[r - 1][c] == word[idx + 1]
        ):
            ch = board[r - 1][c]
            board[r - 1][c] = "0"
            up = self.isExist(board, word, r - 1, c, idx + 1)
            board[r - 1][c] = ch

        if (
            r < len(board) - 1
            and idx < len(word) - 1
            and board[r + 1][c] == word[idx + 1]
        ):
            ch = board[r + 1][c]
            board[r + 1][c] = "0"
            down = self.isExist(board, word, r + 1, c, idx + 1)
            board[r + 1][c] = ch

        if (
            c > 0
            and idx < len(word) - 1
            and board[r][c - 1] == word[idx + 1]
        ):
            ch = board[r][c - 1]
            board[r][c - 1] = "0"
            left = self.isExist(board, word, r, c - 1, idx + 1)
            board[r][c - 1] = ch

        if (
            c < len(board[0]) - 1
            and idx < len(word) - 1
            and board[r][c + 1] == word[idx + 1]
        ):
            ch = board[r][c + 1]
            board[r][c + 1] = "0"
            right = self.isExist(board, word, r, c + 1, idx + 1)
            board[r][c + 1] = ch

        return up or down or left or right