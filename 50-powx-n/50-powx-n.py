class Solution(object):
    
    def myPow(self, x, n):

        """
        :type x: float
        :type n: int
        :rtype: float
        """
        b=0
        if n<0:
            n=-n
            x=1/x
        if n==0:
            return 1
        b=self.myPow(x,n/2)
        if n%2==0:
            # while ((n/2)>0):
            #     b=b*x
            #     n-=1
            return b*b
        else:
            # while ((n/2)>0):
            #     b=b*x
            #     n-=1
            return b*b*x
            
        
            
            