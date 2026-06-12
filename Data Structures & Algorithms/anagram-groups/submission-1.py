class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                ind = ord(c) - ord('a')
                key[ind] += 1
            mapping[tuple(key)].append(s)

        return [values for values in mapping.values()]
        