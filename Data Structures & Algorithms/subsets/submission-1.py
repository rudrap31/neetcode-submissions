class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []


        def search(i, cur):
            if i == n:
                res.append(cur[:])
                return
            
            search(i+1, cur)

            cur.append(nums[i])
            search(i+1, cur)
            cur.pop()
            
            
        
        search(0, [])
        return res