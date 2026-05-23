class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_count = Counter(nums)

        mc = nums_count.most_common()
        mc = sorted(mc, key = lambda x: -x[0])
        
        for i in mc:
            if i[1]==1:
                return i[0]
        return -1
        
        