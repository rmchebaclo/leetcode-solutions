class Solution:
    # dfs
    # l = length of the word, m = rows, n = cols
    # time: O(m * n * 4 ^l)
    # space: O(l)
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r, c, i, visited, valid):
            if i == len(word):
                valid[0] = 1
                return
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r,c) in visited or board[r][c] != word[i]):
                return
            visited.add((r,c))
            dfs(r + 1, c, i + 1, visited, valid)
            dfs(r - 1, c, i + 1, visited, valid)
            dfs(r, c + 1, i + 1, visited, valid)
            dfs(r, c - 1, i + 1, visited, valid)
            visited.remove((r,c))
            return valid[0]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set(), [0]) == True:
                        return True
        return False