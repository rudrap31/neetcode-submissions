class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = set()
        l = 0
        r = 0
        m = 0

        while r < len(s):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            m = max(m, r - l + 1)
            r += 1

        return m
