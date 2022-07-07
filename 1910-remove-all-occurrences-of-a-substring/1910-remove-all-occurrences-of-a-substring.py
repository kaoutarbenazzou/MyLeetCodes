class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        l=len(part)
        # s=list(s)
        # part=list(part)
        while True:
            if part in s:
                s=list(s)
                part=list(part)
                for i in range(len(s)):
                    if s[i:i+l]==part:
                        del s[i:i+l]
                        break
                s = "".join(s)
                part = "".join(part)
            else:
                break
        return s