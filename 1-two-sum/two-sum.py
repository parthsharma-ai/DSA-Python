class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,x in enumerate(nums):
            need=target-x
            if need in seen:
                return [seen[need],i]
            seen[x]=i
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        