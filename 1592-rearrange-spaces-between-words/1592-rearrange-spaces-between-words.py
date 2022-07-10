class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        count=0
        for i in text:
            if i==' ':
                count+=1
        words=text.split()
        l=len(words)
        if(l==1):
            return words[0]+(' '*count)
        n=count//(l-1)
        text=words[0]
        del words[0]
        for i in words:
            text=text+(' '*n)+i
        #n=count-n*(l-1)
        return text+(' '*(count%(l-1)))
       
        
        
        