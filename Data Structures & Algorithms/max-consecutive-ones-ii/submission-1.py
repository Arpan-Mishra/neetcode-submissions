class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if 0 not in nums:
            return len(nums)
        
        l = 0

        max_1s = 0
        count_1s = max_1s
        count_z = 0
        k = 1

        for r in range(len(nums)):
            if nums[r]:
                count_1s+=1
            else:
                count_z+=1
            while count_z>k:
                
                if nums[l]:
                    count_1s-=1
                else:
                    count_z-=1
                
                l+=1
            
            max_1s = max(count_1s, max_1s)
        
        return max_1s+1



