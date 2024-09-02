from collections import deque
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = distance
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r >= 0 and new_c >= 0 and 
                        new_r < rows and new_c < cols
                        and (new_r, new_c) not in visited 
                        and rooms[new_r][new_c] != -1):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            distance += 1