from tree_node import TreeNode
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        # Preorder recursive dfs
        # time complexity: O(n)
        # space complexity: O(h), height = n in worst case when tree isn't balanced
        def recur(node, path):
            if not node:
                return
            path.append(str(node.val))
            # add path to result when at a leaf
            if not node.right and not node.left:
                all_paths.append("->".join(path))
            recur(node.left, path)
            recur(node.right, path)
            # pop node off of path once recursive calls end
            path.pop()  
        all_paths = []
        recur(root, [])
        return all_paths