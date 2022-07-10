class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(1,len(nums)+1):
            x=0
            for j in range(i):
                x+=nums[j]
            l.append(x)
        return l