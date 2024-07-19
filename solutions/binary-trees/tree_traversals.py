from tree_node import TreeNode
class Solution:
    # same complexity for all traversals 
    # time complexity: 0(n)
    # space complexity: O(h), h = logn in balanced tree, h = n in worst case
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def inorderRecur(root, stack):
            if not root: 
                return 
            inorderRecur(root.left, stack)
            stack.append(root.val)
            inorderRecur(root.right, stack)
        stack = []
        inorderRecur(root, stack)
        return stack
    
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def postorderRecur(root, stack):
            if not root: 
                return 
            postorderRecur(root.left, stack)
            postorderRecur(root.right, stack)
            stack.append(root.val)
        stack = []
        postorderRecur(root, stack)
        return stack
    
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        def preorderRecur(root, stack):
            if not root: 
                return 0
            stack.append(root.val)
            preorderRecur(root.left, stack)
            preorderRecur(root.right, stack)
        stack = []
        preorderRecur(root, stack)
        return stack