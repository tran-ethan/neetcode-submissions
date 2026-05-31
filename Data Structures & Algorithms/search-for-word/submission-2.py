class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def dfs(row, col, i):
            if i == len(word) - 1:
                return True
            
            t = l = r = b = False
            # check top
            if row != 0:
                if board[row - 1][col] == word[i + 1] and (row - 1, col) not in seen:
                    seen.add((row - 1, col))
                    t = dfs(row - 1, col, i + 1)
                    seen.remove((row - 1, col))
            
            # check left
            if col != 0:
                if board[row][col - 1] == word[i + 1] and (row, col - 1) not in seen:
                    seen.add((row, col - 1))
                    l = dfs(row, col - 1, i + 1)
                    seen.remove((row, col - 1))

            # check right
            if col != len(board[0]) - 1:
                if board[row][col + 1] == word[i + 1] and (row, col + 1) not in seen:
                    seen.add((row, col + 1))
                    r = dfs(row, col + 1, i + 1)
                    seen.remove((row, col + 1))

            # check bottom
            if row != len(board) - 1:
                if board[row + 1][col] == word[i + 1] and (row + 1, col) not in seen:
                    seen.add((row + 1, col))
                    b = dfs(row + 1, col, i + 1)
                    seen.remove((row + 1, col))

            return t or l or r or b # if any recursive calls

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    seen.add((row, col))
                    found = dfs(row, col, 0)
                    seen.remove((row, col))

                    if found:
                        return True

        return False
        