class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in s
        for x in s:
            freq[x] = freq.get(x, 0) + 1

        # Subtract characters using t
        for i in t:
            if i not in freq:
                return False

            freq[i] -= 1

        # Every frequency must be zero
        for x in freq:
            if freq[x] != 0:
                return False

        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        