class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def dfs(target):
            if target == "":
                return True
            if target in memo:
                return memo[target]
            
            for word in wordDict:
                n = len(word)
                if n > len(target):
                    continue
                
                if word == target[:n]:
                    memo[target] = dfs(target[n:])
                    if memo[target]:
                        return True
            
            return False
        
        return dfs(s)
                