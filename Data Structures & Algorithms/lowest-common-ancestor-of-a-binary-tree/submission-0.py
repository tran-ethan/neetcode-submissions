# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def dfs(node):
            if not node:
                return (False, False)

            hasPL, hasQL = dfs(node.left)
            hasPR, hasQR = dfs(node.right)

            hasQ = hasQL or hasQR
            hasP = hasPL or hasPR

            if p == node:
                hasP = True
            if node == q:
                hasQ = True
            
            if self.res is None and hasP and hasQ:
                # this is the one we're looking for
                self.res = node
                return (True, True)

            return (hasP, hasQ)

        dfs(root)
        return self.res