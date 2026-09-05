class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def r(cur, total, i):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            r(cur, total+nums[i], i)
            cur.pop()

            r(cur, total, i+1)

        
        r([], 0, 0)
        return res

        
        