class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        freq={}
        window={}
        l=0
        for x in s1:
            freq[x]=freq.get(x,0)+1
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if r-l+1==len(s1):
                if window==freq:
                    return True
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l+=1
        return False        

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        