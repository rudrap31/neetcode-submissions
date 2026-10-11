class Solution:
    def trap(self, height: List[int]) -> int:


        n = len(height)
        lmax = [0] * n
        rmax = [0] * n

        for i in range(n):
            if i == 0:
                lmax[i] = 0
                continue
            lmax[i] = max(lmax[i-1], height[i-1])

        for j in range(n - 1, 0, -1):
            if j == n - 1:
                rmax[j] = 0
                continue
            rmax[j] = max(rmax[j+1], height[j+1])

        water = 0

        for i in range(n):
            water += max(min(lmax[i], rmax[i]) - height[i], 0)
        
        return water


        