class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ###create a new matrix for summation with 1 more row and 1 more column
        if not matrix: return None
        self.nrow=len(matrix)
        
        if not matrix[0]: return None
        self.ncol=len(matrix[0])

        
        self.summatrix=[[0 for j in range(self.ncol+1)] for i in range(self.nrow+1)]
        
        ##remember to get original element in summatrix[i][j], we need to trace back in matrix[i-1][j-1]
        for i in range(1,self.nrow+1):
            for j in range(1,self.ncol+1):
                self.summatrix[i][j]=self.summatrix[i-1][j]+self.summatrix[i][j-1]-self.summatrix[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        
        return self.summatrix[row1][col1]+self.summatrix[row2+1][col2+1]-self.summatrix[row1][col2+1]-self.summatrix[row2+1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)