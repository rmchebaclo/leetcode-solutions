from tree_node import TreeNode
class Solution:
    # recursive dfs
    # time complexity: O(n)
    # space complexity: O(h), h = n in worst case when tree isn't balanced
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    dfs(left.right, right.left) and 
                    dfs(left.left, right.right))
        return dfs(root.left, root.right)