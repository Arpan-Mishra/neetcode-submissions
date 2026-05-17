class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        freq = Counter(nums)
        
        if freq.most_common()[0][1]>1:
            return True
        else:
            return False