# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])

        while q:
            COUNT = len(q)
            layer = []
            for i in range(COUNT):
                v = q.popleft()
                layer.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
                
            result.append(layer)

        return result