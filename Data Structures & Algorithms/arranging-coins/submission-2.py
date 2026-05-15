class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n-1

        while l<=r:
            m = (l+r)//2
            sm = (m+1)*(m+2)/2

            if sm==n:
                return m + 1
            elif sm<n:
                l = m+1
            else:
                r = m-1
        
        return r + 1






        