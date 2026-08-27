class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=0
        l=0
        max_sum=float('-inf')
        for r in range(len(nums)):
            window_sum+=nums[r]
            if r-l+1==k:
                max_sum = max(max_sum, window_sum)
                window_sum-=nums[l]
                l+=1
        return max_sum/float(k)


        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        