# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            return l.val == r.val and self.isSameTree(l.left, r.left) and self.isSameTree(l.right, r.right) 
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(subRoot, root.left) or self.isSameTree(subRoot, root.right):
            return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        if self.isSameTree(root, subRoot):
            return True

        return False

        
