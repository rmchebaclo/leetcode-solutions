"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# dfs
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(og, clone, seen):
            if not og or og in seen:
                return
            visited[og] = clone
            for neighbor in og.neighbors:
                if neighbor in visited:
                    clone.neighbors.append(visited[neighbor])
                else:
                    neighbor_clone = Node(neighbor.val, [])
                    clone.neighbors.append(neighbor_clone)
                    dfs(neighbor, neighbor_clone, seen)
        
        if not node:
            return
        visited = {}
        first = Node(node.val,[])
        dfs(node, first, visited)
        return first
    
    # bfs
    # time: O(n)
    # space: O(n)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        start = Node(node.val, [])   
        visited = {node: start}
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor in visited:
                        visited[curr].neighbors.append(visited[neighbor])
                    else:
                        clone = Node(neighbor.val, [])
                        visited[neighbor] = clone
                        visited[curr].neighbors.append(clone)
                        queue.append(neighbor)
        return start