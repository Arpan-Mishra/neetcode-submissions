class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        cur_great = arr[-1]
        res = [0]*len(arr)
        res[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            val = arr[i]
            res[i] = cur_great
            if val>cur_great:
                cur_great = val
            
        return res
            
            