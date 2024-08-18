class Solution:
    '''
    matrix dfs solution
    assuming that altering the matrix to record visited cells is okay
    if not we can use a hashset to hold visited cells

    time complexity: O(4^n*m) that is the amount of possible paths
    as we can go up, down, left, or right for each cell in the matrix
    assuming they are all unblocked
    
    space complexity: O(1) or O(m * n) if we use a hashset
    '''
    def countPaths(self, grid: list[list[int]]) -> int:
        def dfs(grid, r, c):
            rows, cols = len(grid), len(grid[0])
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or grid[r][c] == 1):
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            total = 0
            grid[r][c] = 1
            total += dfs(grid, r + 1, c)
            total += dfs(grid, r - 1, c)
            total += dfs(grid, r, c + 1)
            total += dfs(grid, r, c - 1)
            grid[r][c] = 0
            return total
            
        return dfs(grid, 0, 0)