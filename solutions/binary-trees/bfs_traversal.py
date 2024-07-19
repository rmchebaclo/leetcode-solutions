from tree_node import TreeNode
from collections import deque
class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def bfs(self, root: TreeNode) -> list[list[int]]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        # process each level of the tree
        while len(queue) > 0:
            level = []
            # process each node and children of that node of given level
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)
        return res