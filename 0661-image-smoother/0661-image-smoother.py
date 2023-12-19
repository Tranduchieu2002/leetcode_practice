class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0] *  m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                sum_area = 0
                cells_number = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        next_col = c + dc
                        next_row = r + dr
                        if next_col < 0 or next_col >= m or next_row < 0 or next_row >= n:
                            continue
                        
                        sum_area += img[next_row][next_col]
                        cells_number += 1
                ans[r][c] = sum_area // cells_number
        
        return ans