class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        m=len(mat)
        n=len(mat[0])
        mm=[]
        p=[]
        s=[]

        if (m*n) != (r*c):
            return (mat)

        else:

            for i in mat:
                for j in i:
                     mm.append(j)
            
            for dd in range(r):
                for l in range(c):
                    s.append(mm[0])
                    mm.pop(0)
                    
                p.append(list(s))
                s=[]
            return (p) 
        