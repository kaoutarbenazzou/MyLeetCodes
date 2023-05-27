class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l=[]
        # for i in range(len(nums)):
        #     l.append(nums[:i]+nums[i+1:])
        # for k in range(len(l)):
        #     l[k]=reduce((lambda x, y: x * y), l[k])
        # return l
        # l=[]
        # for i in range(len(nums)):
        #     l.extend(nums[:i]+nums[i+1:])
        # print(l)
        # hop=len(nums)-1
        # j=-1
        # nums[j]=l[0]

        #another time exceeded code:
        """for i in range(0,len(l)):
            if (i)%hop==0 and j<hop:
                j+=1
                #print('i',i,j,l[i])
                nums[j]=l[i]
            else:  
                nums[j]*=l[i]
                
            #print(nums)
        
        return nums"""
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)

            
