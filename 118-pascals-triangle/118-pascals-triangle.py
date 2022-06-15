import math
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        m=[]
        if numRows==1:
            a=[[1]]
            return a
        elif numRows==2:
            b=[[1],[1,1]]
            return b
        else:
            b=[[1],[1,1]]
            for i in range(2,numRows):
                b.append(list())
            for n in range(2, numRows):
                #print('n',n)
                b[n].insert(0,1)
                b[n].insert(n-1,1)
                for k in range(1,n):
                    #print('k',k)
                    x=b[n-1][k-1]+b[n-1][k]
                    b[n].insert(k,x)
        
                
                
        return b

                
                
            
            