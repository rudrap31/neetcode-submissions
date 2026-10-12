class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(cur, l,r):
            if l == n and r == n:
                res.append(cur[:])
                return
            
            if l < n:
                cur += "("
                backtrack(cur, l+1, r)
                cur = cur[:-1]
            
            if r < n and r < l:
                cur += ")"
                backtrack(cur, l, r+1)
                cur = cur[:-1]
            


            
        backtrack("", 0, 0)
        return res


        