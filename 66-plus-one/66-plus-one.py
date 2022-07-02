class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(e) for e in digits)
        s=int(s)
        s+=1
        return list(str(s))
        