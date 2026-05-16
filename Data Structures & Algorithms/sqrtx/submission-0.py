class Solution:
    def mySqrt(self, x: int) -> int:
        
        res = -1
        l = 0
        r = x

        while l<=r:
            m = (l+r)//2

            sq = m*m

            if sq==x:
                return m
            elif sq>x:
                r = m-1
            else:
                res = max(res, m)
                l = m+1
            
        
        return res
                
            
            


        