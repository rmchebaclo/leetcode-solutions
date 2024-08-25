from collections import deque
class Solution:
    # bfs
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r >= 0 and new_c >= 0 and new_r < rows
                        and new_c < cols and grid[new_r][new_c] == "1"
                        and ((new_r,new_c)) not in visited):
                        queue.append((new_r,new_c))
                        visited.add((new_r,new_c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
    # dfs
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or grid[r][c] == "0" or (r,c) in visited):
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands
    