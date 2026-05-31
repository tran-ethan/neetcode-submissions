class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        if not s:
            return []
        res = []

        length = -1
        lengthStr = "" # Used to stored length when iterating over
        word = ""
        for i, char in enumerate(s):
            # If length > 0, we are reading the word
            if length > 0:
                word += char
                length -= 1
            # If length  0, that means that we reading the number following the word
            else:
                # Stop reading length
                if char == "#":
                    if length != -1:
                        res.append(word)
                        word = ""
                    length = int(lengthStr)
                    lengthStr = ""
                else:
                    lengthStr += char

        res.append(word)

        return res
