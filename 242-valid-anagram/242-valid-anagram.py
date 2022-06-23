class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                #print(i)
                if i in t:
                    t.remove(i)
                    #print(t)

        if t==[]:
            return True
        else:
            return False
        