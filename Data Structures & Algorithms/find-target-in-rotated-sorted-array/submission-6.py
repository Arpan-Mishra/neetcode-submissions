class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2

            if nums[m]==target:
                return m
            
            elif nums[m]>=nums[l]: 
                # we are in left sorted array
                if target >= nums[l] and target < nums[m]:
                    # search left
                    r = m - 1
                else:
                    # search right
                    l = m + 1
            else:
                # in right sorted array
                if target > nums[m] and target <= nums[r]:
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1
        return -1