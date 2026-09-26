from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        q = deque()


        def rotn(i, j):
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]
             
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if ni >= n or ni < 0 or nj >= m or nj < 0: 
                    continue
                if grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni,nj))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])
        
        step = -1
        while len(q) > 0:
            for h in range(len(q)):
                rotn(q[0][0],q[0][1])
                q.popleft()
            step+=1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max(step,0)
        



        