class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if nums.count(i)==2:
                l.append(i)
                break
        for i in range(len(nums)):
            if i+1 not in nums:
                l.append(i+1)
                break
        return l
        