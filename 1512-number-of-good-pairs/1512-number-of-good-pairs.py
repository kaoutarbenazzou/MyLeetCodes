class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        c=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            c+=i*(i-1)//2
        return c