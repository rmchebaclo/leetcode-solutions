from tree_node import TreeNode
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        # recursive dfs 
        # time complexity: O(n)
        # space complexity: O(h) = logn because we are building a balanced tree
        def recur(l, r):
            if l > r:
                return 
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = recur(l, m - 1)
            root.right = recur(m + 1 , r)
            return root
        return recur(0, len(nums) - 1)
