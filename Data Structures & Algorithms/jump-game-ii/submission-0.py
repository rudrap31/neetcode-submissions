class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [float('inf') for n in nums]
        dp[0] = 0
        cur = 0

        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i+j < len(nums):
                    dp[i + j] = min(dp[i] + 1 , dp[i+j])
        
        return dp[-1]

        