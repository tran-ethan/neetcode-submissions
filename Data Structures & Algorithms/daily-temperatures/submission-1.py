class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # (i, temperature)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            # keep popping until no elements or next element is greater
            while stack and stack[-1][1] <= temp:
                stack.pop()
            
            if stack:
                # there is element greater than current temp
                diff = stack[-1][0] - i
                result[i] = diff
            else:
                # no greater element than current temp
                result[i] = 0

            stack.append((i, temp))

        return result

            