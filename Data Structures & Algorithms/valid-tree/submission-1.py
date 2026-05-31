class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {i: [] for i in range(n)}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        gray = set()
    
        def dfs(caller, node):
            if node in gray:
                return False

            gray.add(node)
            for neighbor in tree[node]:
                if neighbor != caller:
                    if not dfs(node, neighbor):
                        return False

            return True

        if not dfs(-1, 0):
            return False
        
        return len(gray) == n

            