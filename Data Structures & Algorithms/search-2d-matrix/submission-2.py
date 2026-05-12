class Solution:
    
    def binary_search(self, target, nums):
        left = 0
        right = len(nums) - 1
        
        while left<=right:
            mid = (left + (right-left)//2)

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_nums = [i[0] for i in matrix]
        l = 0
        r = len(row_nums) - 1

        while l<=r:
            mid = (l + (r-l)//2)
            if row_nums[mid]==target:
                return True
            elif row_nums[mid]>target:
                r = mid - 1
            else:
                l = mid+1
            
            

        ri = r
        if ri < 0:
            return False
        nums = matrix[ri]
        if self.binary_search(target, nums):
            return True
        else:
            return False