class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            nums.extend(row)
        
        left,right = 0,len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                return True
        return False