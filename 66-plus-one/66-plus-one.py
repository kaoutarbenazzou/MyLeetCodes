class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # i=-1
        # while i!=-len(digits):
        #     k=i
        def addi(digits, k=-1):
            n=(digits[k]+1)%10
            if (n!=0):
                digits[k]+=1
            else:
                digits[k]=0
                try:
                    addi(digits, k-1)
                except:
                    digits.insert(0,0)
                    addi(digits,k-1)
        addi(digits)
        return(digits)

            
        