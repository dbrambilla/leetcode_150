class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable_set, prev_height):
            # Out of bounds, already visited, or flowing downhill (invalid in reverse)
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in reachable_set or heights[r][c] < prev_height):
                return
            
            # Mark current cell as reachable from this ocean
            reachable_set.add((r, c))
            
            # Traverse uphill to 4 neighbors
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])
            
        # 1. Start DFS from horizontal borders (Top row -> Pacific, Bottom row -> Atlantic)
        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])
            
        # 2. Start DFS from vertical borders (Left col -> Pacific, Right col -> Atlantic)
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])
            
        # 3. Find the intersection where cells can reach both oceans
        return list(pacific_reachable.intersection(atlantic_reachable))
