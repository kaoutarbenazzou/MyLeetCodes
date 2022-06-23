class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r= list(ransomNote)
        m=list(magazine)
        flag=0

        if len(r)>len(m):
            return False
        else:
            for i in (r):
                if i in m:
                    m.remove(i)
                else:
                    flag=1
                    break
        if flag==0:       
            return True
        else:
            return False
        