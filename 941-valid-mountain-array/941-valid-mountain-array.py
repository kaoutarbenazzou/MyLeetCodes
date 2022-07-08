class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flag=0
        count=0
        max=arr[0]
        i=0
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                max=arr[i]
                flag=1
                break
            elif(arr[i]<arr[i-1] or arr[i]==arr[i-1]):
                flag=0
                break
        if i<len(arr):    
            for j in range(i+1,len(arr)):
                if arr[j]<arr[j-1] and flag==1:
                    continue
                else:
                    flag=0
                    break         
        
        if flag==1:
            return True
        else:
            return False
    
    
        