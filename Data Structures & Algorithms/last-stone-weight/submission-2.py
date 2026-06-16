class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-stone for stone in stones]
        heapq.heapify(weights)

        while len(weights) >= 2:
            max1 = heapq.heappop(weights)
            max2 = heapq.heappop(weights)

            if max1 > max2:
                heapq.heappush(weights, max2 - max1)
            elif max2 > max1:
                heapq.heappush(weights, max1 - max2)
        
        if weights:
            return -weights[0]
        return 0
