class Solution(object):
    def longestConsecutive(self, nums):
        max_length=0
        seq=set(nums)
        for x in seq:
            if x-1 not in seq:
                current=x
                length=1
                while current+1 in seq:
                    current+=1
                    length+=1
                max_length = max(max_length, length)
        return max_length
       


        """
        :type nums: List[int]
        :rtype: int
        """
        