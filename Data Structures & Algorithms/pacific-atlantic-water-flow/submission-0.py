class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        n = len(heights)
        m = len(heights[0])
        pv = set()
        av = set()

        def traverse(row, col, ov):
            if (row, col) in ov:
                return
            ov.add((row,col))
            
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]

            for r,c in dirs:
                x = row + r
                y = col + c

                if 0 > x or x >= n or 0 > y or y >= m:
                    continue

                if heights[x][y] >= heights[row][col]:
                    
                    traverse(x,y,ov)


        for i in range(n):
            traverse(i, 0, pv)
            traverse(i, m-1, av)

        for i in range(m):
            traverse(0, i, pv)
            traverse(n-1, i, av)

        arr = []
        for a,b in pv:
            if (a,b) in av:
                arr.append([a,b])
        
        return arr

        
        

        