class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        d = (arr[-1] - arr[0])/len(arr)

        l = 0
        r = len(arr)-1

        # AP: a, a+d, a+2d, ...

        while l<=r:

            m = (l+r)//2

            if arr[m] == (arr[0] + (m)*d):
                # all until m correct, search right
                l = m+1
            else:
                r = m-1
        
        
        
        
        return int(arr[0] + max(m,l)*d)









        return 0
            
