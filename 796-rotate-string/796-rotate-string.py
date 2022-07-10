class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s=list(s)
        goal=list(goal)
        for i in range(len(s)):
            if(s==goal):
                return True
            else:
                temp=s[0]
                for j in range(len(s)-1):
                    s[j]=s[j+1]
                s[len(s)-1]=temp
        return False
                
        