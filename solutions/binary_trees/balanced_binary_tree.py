from tree_node import TreeNode
class Solution:
    # postorder recursive dfs, bottom up solution 
    # time complexity: O(n)
    # space complexity: O(h), h = n in worst case: unbalanced tree
    def isBalanced(self, root: TreeNode) -> bool:
        def balance_and_depth(root):
            if not root:
                return (0, True)
            depth_l, balance_l = balance_and_depth(root.left)
            depth_r, balance_r = balance_and_depth(root.right)
            curr_balanced = balance_l and balance_r and abs(depth_l - depth_r) <= 1
            curr_depth = 1 + max(depth_l, depth_r)
            return (curr_depth, curr_balanced)
        return balance_and_depth(root)[1]
    
    # inorder recursive dfs
    # time complexity: O(n^2)
    # space complexity: O(h), h = n in worst case: unbalanced tree
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        depth_l = self.depth(root.left)
        depth_r = self.depth(root.right)
        return (abs(depth_l - depth_r) <= 1 and self.isBalanced(root.left)
            and self.isBalanced(root.right))
    
    # helper to calculate depth of subtree
    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))