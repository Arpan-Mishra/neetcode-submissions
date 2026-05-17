class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)>len(t):
            return False
        if not s:
            return True
        
        ci = 0

        sub = ''

        for c in t:
            if c==s[ci]:
                sub+=c
                ci+=1
            
            if s==sub:
                return True
            
        
        return False
        
