class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        if needle=="":
            return 0
        
        for i in range(len(haystack)):
            if haystack[i]== needle[0]:
                if haystack[i:i+len(needle)]==needle :
                    return i
            
        
        