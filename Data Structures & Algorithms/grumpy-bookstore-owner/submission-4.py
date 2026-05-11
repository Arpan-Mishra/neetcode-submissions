class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        satisfied = sum([customers[i] for i in range(len(customers)) if not grumpy[i]])
        sat = max_sat = sum([customers[i] for i in range(len(customers[l:minutes])) if grumpy[i]])


        for r in range(minutes, len(customers)):
            
            if grumpy[r]:
                sat = sat + customers[r]
            if grumpy[l]:
                sat-=customers[l]

            max_sat = max(sat, max_sat)
            l+=1
        return satisfied+max_sat
        
            
        




        