class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # (i, temperature)
        
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, tmp = stack.pop()
                result[i] = index - i
            stack.append((index, temp))
        
        return result
            