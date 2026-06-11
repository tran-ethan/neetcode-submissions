# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        diff = [True]

        def height(node):
            if not node:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)
            if abs(leftHeight - rightHeight) > 1:
                # print(f"{node.val}: leftH: {leftHeight}, rightH: {rightHeight}")
                diff[0] = False

            return 1 + max(leftHeight, rightHeight)

        height(root)
        return diff[0]