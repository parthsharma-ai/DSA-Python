class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        l_sum=0
        for i in range(len(nums)):
            r_sum=total-l_sum-nums[i]
            if l_sum==r_sum:
                return i
            l_sum += nums[i]
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        