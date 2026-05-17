class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0


        for i in range(len(s)-1):
            
            abs_dif = abs(ord(s[i+1]) - ord(s[i]))
            
            score+=abs_dif
        
        return score





