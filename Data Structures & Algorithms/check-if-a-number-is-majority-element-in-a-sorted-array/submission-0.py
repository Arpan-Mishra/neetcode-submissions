class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        th = len(nums)/2

        cnt = Counter(nums)

        count_num = cnt.get(target, 0)
        if count_num>th:
            return True
        else:
            return False
