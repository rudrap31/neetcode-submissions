class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dp = []
        for i in range(len(s)+ 1):
            dp.append([])

        dp[len(s)] = [""]
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                n = len(word)
                if word == s[i:i+n]:
                    for rest in dp[i + n]:
                        if rest != "":
                            dp[i].append(word + " " + rest)
                        else:
                            dp[i].append(word)
        return dp[0]
