class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            mapping[str(sorted(s))].append(s)

        return [v for v in mapping.values()]
        