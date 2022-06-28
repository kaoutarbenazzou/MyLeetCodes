class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d={}
        listt=[]
        l=0
        f=0
        # for hi in len(mat):
        #     d[hi]=0
        for i in mat:
            counter=0
            for j in i:
                if(j==1):
                    counter+=1
            d[l]=counter
            l+=1
        while f!=k:
            minv = min(d.values()) 
            for key,value in d.items():
                if value==minv:
                    listt.append(key)
                    del d[key]
                    break
            f+=1
        return listt
            
                    
        
        
            
                    
                    
                
                    
            
            