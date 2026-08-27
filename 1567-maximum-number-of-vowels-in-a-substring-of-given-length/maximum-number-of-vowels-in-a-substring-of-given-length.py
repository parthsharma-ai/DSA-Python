class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        count = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            # Add new character
            if s[right] in vowels:
                count += 1

            # When window reaches size k
            if right - left + 1 == k:
                max_count = max(max_count, count)

                # Remove left character
                if s[left] in vowels:
                    count -= 1

                left += 1

        return max_count
     

                



        """
        :type s: str
        :type k: int
        :rtype: int
        """
        