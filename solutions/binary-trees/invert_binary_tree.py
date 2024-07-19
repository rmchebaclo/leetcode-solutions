from tree_node import TreeNode
from collections import deque
class Solution:
    # recursive dfs approach
    # time complexity: O(n)
    # space complexity: O(h), h = logn in balanced tree, h = n in worst case
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    # iterative bfs
    # time complexity: O(n)
    # space complexity: O(w), width of the tree worse case w = n
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                tmp = curr.left
                curr.left = curr.right
                curr.right = tmp
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root