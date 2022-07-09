class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x=list(str(x))
        l=len(x)
        if(l==1):
            return True
        if l%2==0:
            k=l-1
            for i in range(l//2):
                if(x[i]!=x[k]):
                    return False
                k-=1
        else:
            k=l-1
            for i in range((l//2)+1):
                if(x[i]!=x[k]):
                    return False
                k-=1
        return True
                
                    