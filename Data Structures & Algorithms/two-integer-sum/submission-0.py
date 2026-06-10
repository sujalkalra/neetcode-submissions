class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cmap = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in cmap:
                return [cmap[complement],i]
            cmap[num]=i
        return []
            
