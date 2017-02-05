class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:return 0
        m=len(grid)
        n=len(grid[0])
        stack=[];
        cnt=0;
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    pass
                else:
                    cnt+=1
                    stack.append([i,j])
                while stack:
                    ii,jj=stack.pop()
                    
                    if ii>=1 and grid[ii-1][jj]=="1":
                        stack.append([ii-1,jj])
                    
                    if jj>=1 and grid[ii][jj-1]=="1":
                        stack.append([ii,jj-1])
                        
                    if ii<m-1 and grid[ii+1][jj]=="1":
                        stack.append([ii+1,jj])

                    if jj<n-1 and grid[ii][jj+1]=="1":
                        stack.append([ii,jj+1])
                    
                    grid[ii][jj]="0"
        return cnt
                    
                    