class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = set(nums)
        return len(contains) != len(nums)