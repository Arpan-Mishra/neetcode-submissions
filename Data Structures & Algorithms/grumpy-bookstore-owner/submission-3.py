class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
       
        max_satisfied = 0

        l = 0
        window = 0

        satisfied = 0

        for r in range(len(customers)):
            

            if grumpy[r]==0:
                satisfied+=customers[r]
            else:
                window+=customers[r]
            
            if r-l+1>minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            
            max_satisfied = max(window, max_satisfied)
        
        satisfied+=max_satisfied







        
        return satisfied



            

            
            


        