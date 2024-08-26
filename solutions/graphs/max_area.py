from collections import deque
class Solution:
    # dfs
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
            max_area = 0
            visited = set()
            rows, cols = len(grid), len(grid[0])
            def dfs(r, c, total):
                if (r < 0 or c < 0 or r >= rows or c >= cols
                    or (r,c) in visited or grid[r][c] == 0):
                    return total[0]
                visited.add((r,c))
                total[0] += 1
                dfs(r + 1, c, total)
                dfs(r - 1, c, total)
                dfs(r, c + 1, total)
                dfs(r, c - 1, total)
                return total[0]
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        max_area = max(max_area, dfs(r,c, [0]))
            return max_area
    # bfs
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            area = 1
            queue = deque()
            queue.append((r,c))
            visited.add((r, c))
            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r >= 0 and new_c >= 0 and 
                        new_r < rows and new_c < cols and
                        (new_r, new_c) not in visited and 
                        grid[new_r][new_c] == 1):
                        area += 1
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r,c))
        return max_area
        