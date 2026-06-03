class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        objective = defaultdict(int)
        counts = defaultdict(int)

        if len(s1) > len(s2):
            return False

        for c in s1:
            objective[c] += 1


        r = 0
        l = 0

        # open window
        while r < len(s1):
            counts[s2[r]] += 1
            r += 1
        
        # slide fixed-size window across
        while r < len(s2):
            # print(counts)
            if self.compare(objective, counts):
                return True
            
            counts[s2[l]] -= 1
            counts[s2[r]] += 1
            l += 1
            r += 1

        # print(counts)
        if self.compare(objective, counts):
            return True
        return False

    def compare(self, m1, m2):
        for k in m1:
            if k not in m2 or m1[k] != m2[k]:
                return False

        return True