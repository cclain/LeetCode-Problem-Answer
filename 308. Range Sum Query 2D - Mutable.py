
### In this program, we only need record of the summation of each row, hence easy for update
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        if not matrix:return None
        if not matrix[0]: return None
        self.nrow=len(matrix)
        self.ncol=len(matrix[0])
        for row in matrix:
            for j in range(1,self.ncol):
                row[j]+=row[j-1]
        self.matrix=matrix
        
                
    

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        change=val-(self.matrix[row][col]-(self.matrix[row][col-1] if col>0 else 0))
        
        for j in range(col,self.ncol):
            self.matrix[row][j]+=change

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum=0
        for i in range(row1,row2+1):
            sum+=self.matrix[i][col2]-(self.matrix[i][col1-1] if col1>0 else 0)
     
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


###This solution is no good for mutable matrix, because change too much element is the update function
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        if not matrix:return None
        if not matrix[0]: return None
        self.nrow=len(matrix)
        self.ncol=len(matrix[0])
        
        self.summatrix=[[0 for i in range(self.ncol+1)] for j in range(self.nrow+1)]
        
        for i in range(1,self.nrow+1):
            for j in range(1,self.ncol+1):
                self.summatrix[i][j]=matrix[i-1][j-1]-self.summatrix[i-1][j-1]+self.summatrix[i-1][j]+self.summatrix[i][j-1]
                
    

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        change=val-(self.summatrix[row+1][col+1]+self.summatrix[row][col]-self.summatrix[row][col+1]-self.summatrix[row+1][col])

        for i in range(row+1,self.nrow+1):
            for j in range(col+1,self.ncol+1):
                self.summatrix[i][j]+=change

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
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)