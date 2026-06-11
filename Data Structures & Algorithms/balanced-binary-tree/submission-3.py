# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node:
                return (True, 0)

            diffLeft, leftHeight = height(node.left)
            diffRight, rightHeight = height(node.right)
            if (not diffLeft) or (not diffRight) or (abs(leftHeight - rightHeight) > 1):
                return (False, -1)

            return (True, 1 + max(leftHeight, rightHeight))

        return height(root)[0]