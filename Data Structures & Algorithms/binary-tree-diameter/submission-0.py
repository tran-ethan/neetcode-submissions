# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return max of left diameter, right diameter

        maxDiameter = [0]

        def height(node):
            if node is None:
                return 0
            
            leftHeight = height(node.left)
            rightHeight = height(node.right)

            diameter = leftHeight + rightHeight
            maxDiameter[0] = max(maxDiameter[0], diameter)
            return 1 + max(leftHeight, rightHeight)

        height(root)
        return maxDiameter[0]
