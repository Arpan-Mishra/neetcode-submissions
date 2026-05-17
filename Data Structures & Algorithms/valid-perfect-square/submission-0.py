class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l = 1
        r = num

        # sqaure root will be <=num

        while l<=r:
            m = (l+r)//2
            sq = m*m
            if sq==num:
                return True
            
            elif sq>num:
                r = m-1
            else:
                l = m+1
        
        return False
