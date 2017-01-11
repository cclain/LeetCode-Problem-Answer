class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        '''
        if len(grid)==0:
            return 0
        else:
            maxbomb=0;
            rows=len(grid);
            cols=len(grid[0]);
            for i in range(rows):
                for j in range(cols):
                    templen=0;
                    if grid[i][j]=='W':
                        pass;
                    elif grid[i][j]=='E':
                        pass;
                    else:
                        rowstartl=j;
                        rowstartr=j+1;
                        while(rowstartl>=0 and grid[i][rowstartl]!='W'):
                            if grid[i][rowstartl]=='E':  
                                templen+=1;
                            rowstartl+=-1;
                           
                        while(rowstartr<cols and grid[i][rowstartr]!='W'):
                            if grid[i][rowstartr]=='E':   
                                templen+=1;
                            rowstartr+=1;
                        colstartu=i-1;
                        colstartd=i+1;
                        while(colstartu>=0 and grid[colstartu][j]!='W'):
                            if grid[colstartu][j]=='E':
                                templen+=1;
                            colstartu+=-1;
                        while(colstartd<rows and grid[colstartd][j]!='W'):
                            if grid[colstartd][j]=='E':
                                templen+=1;
                            colstartd+=1;
                        maxbomb=max(maxbomb,templen);
            return maxbomb
            '''

        if not grid: return 0
        if not grid[0]: return 0
        
        # collect row, col info O(m+n)
        row_cnt, col_cnt = len(grid), len(grid[0])
        self.grid = grid
        self.value = [[0]*col_cnt for _ in range(row_cnt)]
        
        # row direction scan, O(m*n)
        for i in range(row_cnt):
            # accumulate toward right
            cnt = 0
            for j in range(col_cnt):
                self.value[i][j] += cnt
                if grid[i][j] == 'E': cnt += 1
                if grid[i][j] == 'W': cnt = 0
            # accumulate toward right
            cnt = 0
            for j in reversed(range(col_cnt)):
                self.value[i][j] += cnt
                if grid[i][j] == 'E': cnt += 1
                if grid[i][j] == 'W': cnt = 0
                    
        # col direction scan, O(m*n)
        for j in (range(col_cnt)):
            # accumulate toward right
            cnt = 0
            for i in range(row_cnt):
                self.value[i][j] += cnt
                if grid[i][j] == 'E': cnt += 1
                if grid[i][j] == 'W': cnt = 0
            # accumulate toward right
            cnt = 0
            for i in reversed(range(row_cnt)):
                self.value[i][j] += cnt
                if grid[i][j] == 'E': cnt += 1
                if grid[i][j] == 'W': cnt = 0
            
        # print(self.value)
        # only empty could be bump
        for i in range(row_cnt):
            for j in range(col_cnt):
                if grid[i][j] != '0':
                    self.value[i][j] = 0
        # print(self.value)
        
        return max([max(v) for v in self.value])
                           
 
 
                           
                           