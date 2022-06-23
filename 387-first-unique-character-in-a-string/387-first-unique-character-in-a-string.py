class Solution:
    def firstUniqChar(self, s: str) -> int:
        t=list(s)
        c={}

        for l in s:
            c[l] = c.get(l,0) + 1

        for word,count in c.items():
            if count==1:
                letter=word
                break
            else:
                letter=-1
        if letter==-1:
            return(-1)
        else:
            for i in range(len(t)):
                if (t[i]==letter):
                    return(i)