class Solution:
    def trap(self, height: List[int]) -> int:


        
        lmax = height[0]
        
        l = 0
        r = len(height) - 1
        rmax = height[r]

        water = 0
        while l < r:
            if lmax <= rmax:
                l += 1
                water += max(lmax - height[l], 0)
                lmax = max(lmax, height[l])
            else:
                r -= 1
                water += max(rmax - height[r], 0)
                rmax = max(rmax, height[r])
            
        
        return water


        