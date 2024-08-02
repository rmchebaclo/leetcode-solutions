from tree_node import TreeNode
class Solution:
    # Preorder dfs
    # time complexity: O(n)
    # space complexity: O(h), h = n in worst case when tree isn't balanced
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            if node.val >= currMax:
                nonlocal count
                count += 1
                currMax = node.val
            dfs(node.left, currMax)
            dfs(node.right, currMax)
            return count
        count = 0
        return dfs(root, root.val)