class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        ri = len(nums)
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2

            if nums[m]>target:
                r = m-1
                ri = m
            else:
                l = m+1
        
        th = len(nums)//2
        print(ri)
        if nums[ri-th-1] == target:
            return True
        else:
            return False

