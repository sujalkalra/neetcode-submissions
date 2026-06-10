class Solution:
    def trap(self, height: List[int]) -> int:
        max_left,max_right = [0]*len(height),[0]*len(height)

        curr = 0
        for i in range(1,len(max_left)):
            curr = max(curr,height[i-1])
            max_left[i] = curr

        curr = 0
        for i in range(len(max_right)-2,-1,-1):
            curr = max(curr,height[i+1])
            max_right[i] = curr

        res = 0
        for i in range(len(height)):
            res += max(0,min(max_left[i],max_right[i])-height[i])
        
        return res