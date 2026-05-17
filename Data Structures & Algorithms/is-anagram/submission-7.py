class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter_s = Counter(s)

        for c in t:
            if c in counter_s:
                counter_s[c]-=1
                if counter_s[c]==0:
                    del counter_s[c]
            else:
                return False
        
        if counter_s:
            return False
        else:
            return True



