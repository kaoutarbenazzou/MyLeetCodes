class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        if k==0:return 1
        a=nums[:len(nums)-k];b=nums[len(nums)-k:];c=b+a
        nums[:] = c
