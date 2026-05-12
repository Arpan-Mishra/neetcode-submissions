class Solution:
    def time_to_eat(self, k, piles):
        return sum([math.ceil(i/k) for i in piles])

    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # piles.sort()
        l = 1
        r = max(piles)
        
        ms = r

        while l<=r:
            m = l + (r-l)//2
            t = self.time_to_eat(m, piles)
            if t>h:
                l = m+1
            elif t<=h:
                ms = m
                r = m-1
        
        return ms