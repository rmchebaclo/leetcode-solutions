from tree_node import TreeNode
from collections import deque
class Solution:
    # recursive dfs, postorder traversal
    # time complexity: 0(n)
    # space complexity: O(h), h = logn in balanced tree, h = n in worst case
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth_l = 1 + self.maxDepth(root.left)
        depth_r = 1 + self.maxDepth(root.left)
        return max(depth_l, depth_r)
    
    # iterative bfs solution
    # time complexity: 0(n)
    # space complexity: O(w), w = width of tree, w = n in worst case
    def maxDepth(self, root: TreeNode) -> int:
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return level
