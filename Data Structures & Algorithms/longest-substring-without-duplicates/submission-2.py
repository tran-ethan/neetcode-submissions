class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        maximum = 0
        for r in range(len(s)):
            while s[r] in window:
                    # remove characters from the left
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
            maximum = max(maximum, r - l + 1)

        return maximum
        