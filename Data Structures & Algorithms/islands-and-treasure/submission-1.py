class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        distance = 1
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            count = len(q)
            for i in range(count):
                r, c = q.popleft()

                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == len(grid) or nc == len(grid[0]) or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = distance
                    q.append((nr ,nc))

            distance += 1

        