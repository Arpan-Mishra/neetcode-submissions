class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        th = len(nums)//2

        while l<=r:

            m = (l+r)//2
           


            if nums[m] == target: 
                

                if m>=len(nums)-1:
                    if nums[m-th]==target:
                        
                        return True
                    else:
                        return False
                    
                    

                
                if nums[m]<nums[m+1]:
                
                    # check 
                    print(m, th)
                    if nums[m-th]==target:
                        
                        return True
                    else:
                        return False
                else: 
                    l = m+1
            
            elif nums[m]>target:
                r = m-1
            
            
            else:
                l = m+1
            

        return False