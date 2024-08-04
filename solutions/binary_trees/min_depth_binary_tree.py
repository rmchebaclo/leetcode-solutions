from tree_node import TreeNode
from collections import deque
class Solution:
    # iterative bfs
    # time complexity: O(n)
    # space complexity: O(w) width = n in worst case
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = deque()
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            depth += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return depth
    
    # recursive dfs
    # time complexity: O(n)
    # space complexity: O(h), h = logn in balanced tree, h = n in worst case
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if  not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)