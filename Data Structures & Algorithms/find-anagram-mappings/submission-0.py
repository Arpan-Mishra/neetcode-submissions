class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        nums2_map = {v:i for (i,v) in enumerate(nums2)}

        for i in range(len(nums1)):
            n = nums1[i]    
            idx_nums2 = nums2_map[n]
            res.append(idx_nums2)
        
        return res



