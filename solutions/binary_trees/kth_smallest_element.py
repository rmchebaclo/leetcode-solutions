from tree_node import TreeNode
class Solution:
    # in order dfs
    # time complexity: O(k), worst case when k = n
    # space complexity: O(h + k)
    # h is the height of the recursive stack, worst case h = n
    # k is the size of the array storing the inorder traversal
    # worst case k = n, so space is O(n) in worst case
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inOrder(node, values):
            if not node or len(values) == k:
                return
            inOrder(node.left, values)
            values.append(node.val)
            inOrder(node.right, values)
        values = []
        inOrder(root, values)
        return values[k-1]
    # iterative in order dfs
    # time complexity: O(n)
    # space complexity: O(n)
    # complexitys have same reasoning as above
    # however there isn't a need for values array alongside recursive stack
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right