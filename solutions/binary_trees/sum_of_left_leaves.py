from tree_node import TreeNode
class Solution:
    def sumOfLeftLeaves(self, root):
        # recursive dfs approach 
        # time complexity: O(n)
        # space complexity: O(h), h = logn in balanced tree, n in worst case
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total