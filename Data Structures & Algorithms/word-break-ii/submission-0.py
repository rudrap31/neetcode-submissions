class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []

        def dfs(target, path):
            if target == "":
                res.append(" ".join(path))
                return 
            
            for word in wordDict:
                n = len(word)
                if n > len(target):
                    continue
                if word == target[:n]:
                    path.append(word)
                    dfs(target[n:], path)
                    path.pop()
            
        
        dfs(s, [])
        return res
        
