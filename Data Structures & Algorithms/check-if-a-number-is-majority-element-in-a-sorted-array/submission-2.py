class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        th = len(nums)/2
        if target in nums:
            i = nums.index(target)
            
            count_num = Counter(nums[i:])[target]
            if count_num>th:
                return True
            return False
        else:
            return False


