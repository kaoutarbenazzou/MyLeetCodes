class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        counter = 0
        count=0

        for i in range (9):
            r=[]
            c=[]
            for j in range(9):
                if board[i][j]!='.':
                    r.append(board[i][j])
                if board[j][i]!='.':
                    c.append(board[j][i])




            if len(set(r)) != len(r) or len(set(c)) != len(c):
                #print('no')
                counter+=1
                break


        for i in range (0,9,3):
            #print(i)
            s=[]
            for j in range(0,9,3):

                #print(j)
                if board[i][j]!='.':
                    s.append(board[i][j])
                if board[i+1][j]!='.':
                    s.append(board[i+1][j])
                if board[i+2][j]!='.':
                    s.append(board[i+2][j])
                if board[i+1][j+1]!='.':
                    s.append(board[i+1][j+1])
                if board[i+1][j+2]!='.':
                    s.append(board[i+1][j+2])
                if board[i+2][j+1]!='.':
                    s.append(board[i+2][j+1])
                if board[i+2][j+2]!='.':
                    s.append(board[i+2][j+2])
                if board[i][j+1]!='.':
                    s.append(board[i][j+1])
                if board[i][j+2]!='.':
                    s.append(board[i][j+2])
                #print(s)
                
                if len(set(s)) != len(s):
                    count+=1
                    #print('count', count)
                s=[]



        if counter>0 or count>0:
            return False
        else:
            return True
