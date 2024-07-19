from tree_node import TreeNode
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
    