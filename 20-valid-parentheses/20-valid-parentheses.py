class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False 
        s=list(s)
        t=[]
        flag=1
        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            flag = 0
            
        for i in s:
            #print(i)
            
            if flag==0:
                break
            if (i=='(' or i=='{' or i=="["):
                t.append(i)
            elif(t == []):
                flag = 0
            
            elif(t!=[]):
                if((t[len(t)-1] == '(' and i == ')') or (t[len(t)-1] == '{' and i == '}') or (t[len(t)-1] == '[' and i == ']')):
                    x=t.pop()
                else:
                    flag = 0
                
                #print('x',x)
                
                

        if flag == 1 and t==[]:
            return True
        else:
            return False
        
        