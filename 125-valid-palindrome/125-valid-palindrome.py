class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if (i.isalpha()):
                l.append(i.lower())
            elif(i.isdigit()):
                l.append(i)
            else:
                continue
        if s=='':
            return True
        if len(l)%2==0:
            k=len(l)-1
            for i in range(len(l)//2):
                if l[i]!=l[k]:
                    return False
                k-=1
        else:
            k=len(l)-1
            for i in range(len(l)//2+1):
                if l[i]!=l[k]:
                    return False
                k-=1   
        return True