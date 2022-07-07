class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        beg=0
        end=k

        l=[]
        for i in range(int(len(s)/k)):
            l.append(s[beg:end])
            beg+=k
            end+=k
        if beg<len(s):
            l.append(s[beg:])
        if len(l[-1])<k:
            l[-1]=l[-1]+(fill)*(k-len(l[-1]))
        return l