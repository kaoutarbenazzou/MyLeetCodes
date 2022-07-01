class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        flag=0  
        i=0
        while i<len(s):
            l=s[i]
            for j in range(1,len(strs)):
                w=strs[j]
                if i<len(w):
                    c=w[i]
                    if (c!=l):
                        flag=1
                        break
                else:
                    flag=1
                    break
            if (flag==1):
                break
            i+=1
        return(s[:i])
        