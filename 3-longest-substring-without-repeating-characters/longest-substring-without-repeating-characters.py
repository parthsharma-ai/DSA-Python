class Solution(object):
      
    def lengthOfLongestSubstring(self, s):
        l = 0
        max_length = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            max_length = max(max_length, r - l + 1)

        return max_length

        """
        :type s: str
        :rtype: int
        """
        