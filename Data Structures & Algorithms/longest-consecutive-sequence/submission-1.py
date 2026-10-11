class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mx = 0
        nset = set(nums)

        for num in nums:
            if num - 1 not in nset:
                length = 1
                while num + length in nset:
                    length += 1
                mx = max(length, mx)
        return mx





        