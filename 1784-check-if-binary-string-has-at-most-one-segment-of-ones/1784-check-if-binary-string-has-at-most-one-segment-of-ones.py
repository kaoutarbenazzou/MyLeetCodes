class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k=list(s)
        if k.count('1')>1:
            i=0
            flag=False
            for i in range(len(s)-1):
                if (s[i]=='1' and s[i+1]=='1'):
                    flag=True
                else:
                    break
            if i<len(s):
                for j in range(i+1,len(s)-1):
                    if(s[j]=='1' ):
                        flag=False
                        break 

            return flag
        else:
            return True