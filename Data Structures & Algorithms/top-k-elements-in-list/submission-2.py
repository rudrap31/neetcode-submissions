class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        n = len(nums)
        counts = {x: set() for x in range(n+1)}

        for num in nums:
            if num in freq:
                cur = freq[num]
                counts[cur].remove(num)
                counts[cur+1].add(num)
                freq[num] += 1
        
            else:
                freq[num] = 1
                counts[1].add(num)

        res = []

        for i in range(n, 0, -1):
            for val in counts[i]:
                res.append(val)
                k -= 1
                if k == 0:
                    return res

        return res


 
