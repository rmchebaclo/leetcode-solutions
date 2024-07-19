from tree_node import TreeNode
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