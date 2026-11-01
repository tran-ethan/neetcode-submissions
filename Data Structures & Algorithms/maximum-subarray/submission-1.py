class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float('-inf')
        res = float('-inf')

        for num in nums:
            if curSum < 0:
                curSum = num
            else:
                curSum += num

            res = max(res, curSum)

        return res
            