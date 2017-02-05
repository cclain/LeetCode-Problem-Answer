class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]], int = 0 dead,1 live
        " 2 dead -> live ; 3 live -> dead
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:return
        m = len(board);
        n=len(board[0])
        if n==0:return
        for i in range(m):
            for j in range(n):
                neighbor=0
                for ii in range(max(0,i-1),min(i+2,m)):
                    for jj in range(max(0,j-1),min(j+2,n)):
                        neighbor+=board[ii][jj]%2
                neighbor-=board[i][j]
                if board[i][j]==1 and (neighbor<2 or neighbor>3):board[i][j]=3
                if board[i][j]==0 and neighbor==3:board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==3:board[i][j]=0
                if board[i][j]==2:board[i][j]=1