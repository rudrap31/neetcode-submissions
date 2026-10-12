class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        dp = {}

        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]

            if ((r - l + 1) % 2 == 0):
                left = piles[l]
                right = piles[r]
                res = max(left + dfs(l + 1, r), right + dfs(l, r - 1))
            else:
                res = min(dfs(l + 1, r), dfs(l, r - 1))
            
            dp[(l,r)] = res
            return res
        
        total = sum(piles)
        alice = dfs(0, len(piles) - 1)
        return alice > total - alice