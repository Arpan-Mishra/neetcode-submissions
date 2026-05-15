class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n==1:
            return 1
        
        for i in range(1, n+1):
            sm = (i*(i+1))/2
            if sm>n:
                break
        return i-1

