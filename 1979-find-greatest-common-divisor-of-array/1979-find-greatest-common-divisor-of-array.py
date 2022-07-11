import sys
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=-sys.maxint-1
        mn=sys.maxint
        div=1
        for i in nums:
            if i<mn:
                mn=i
            if i>mx:
                mx=i
        for i in range(mn*mx,0,-1):
            if mx%i==0 and mn%i==0:
                div=i
                break
        return div
            
            