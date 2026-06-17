class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_map = defaultdict(list)
        heap = []

        for x, y in points:
            distance = math.sqrt(x*x + y*y)
            distance_map[-distance].append([x, y])
            heapq.heappush(heap, -distance)
            if len(heap) > k:
                heapq.heappop(heap)

        return [distance_map[d].pop() for d in heap]