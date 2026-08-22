class Solution(object):
    def groupAnagrams(self, strs):
        grps={}
        for item in strs:
            key=''.join(sorted(item))
            if key not in grps:
                grps[key] = []
            grps[key].append(item)
        return list(grps.values())

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        