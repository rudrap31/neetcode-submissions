class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mp = {}

        for l in s:
            if l in mp:
                mp[l] += 1
            else:
                mp[l] = 1
        
        for l in t:
            if l in mp:
                mp[l] -= 1
            else:
                mp[l] = 1

        for k in mp:
            if mp[k] != 0:
                return False
        return True
            
        