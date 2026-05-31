class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        explore = set()

        def dfs(node):
            if node in explore:
                return

            explore.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        components = 0
        for v in range(n):
            if v not in explore:
                dfs(v)
                components += 1

        return components


            