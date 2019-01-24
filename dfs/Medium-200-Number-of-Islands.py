class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.n = len(grid)
        self.m = len(grid[0])
        self.isVisited = []
        for i in range(self.n):
            self.isVisited.append([])
            for j in range(self.m):
                self.isVisited[-1].append(False)
        def dfs(i, j):
            if self.isVisited[i][j] or grid[i][j] != "1":
                self.isVisited[i][j] = True
                return
            self.isVisited[i][j] = True
            if i+1 < self.n:
                dfs(i+1, j)
            if i-1 >= 0:
                dfs(i-1, j)
            if j + 1 < self.m:
                dfs(i, j+1)
            if j - 1 >= 0:
                dfs(i, j-1)
        
        res = 0
        for i in range(self.n):
            for j in range(self.m):
                if not self.isVisited[i][j] and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res
            