from collections import deque
class Solution:
    # bfs
    # time complexity: O(m * n)
    # time complexityL O(m * n)
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        oranges = 0
        time = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        if oranges == 0:
            return 0
        while queue and oranges > 0:
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r >= 0 and new_c >= 0 and
                        new_r < rows and new_c < cols
                        and grid[new_r][new_c] == 1):
                        oranges -= 1
                        grid[new_r][new_c] = 2
                        queue.append((new_r,new_c))
            time += 1
        if oranges == 0:
            return time
        return -1