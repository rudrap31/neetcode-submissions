class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}
        res = []
        
        for st in strs:
            x = "".join(sorted(st))
            if x in mp:
                mp[x].append(st)
            else:
                mp[x] = [st]
        
        for m in mp:
            res.append(mp[m])

        return res


