class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "ÿ" + s
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("ÿ")[1:]
