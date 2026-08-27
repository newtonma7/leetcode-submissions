class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        cur_row = cur_col = 0
        n = rows * cols
        ans = []
        up = True

        while len(ans) != n:
            if up:
                while cur_row >= 0 and cur_col < cols:
                    ans.append(mat[cur_row][cur_col])
                    cur_row -=1
                    cur_col +=1
                
                if cur_col == cols:
                    cur_row += 2
                    cur_col -= 1
                else:
                    cur_row +=1
                up = False
            else:
                while cur_row < rows and cur_col >= 0:
                    ans.append(mat[cur_row][cur_col])
                    cur_row +=1
                    cur_col -=1
                    
                if cur_row == rows:
                    cur_row -=1
                    cur_col +=2
                else:
                    cur_col += 1
                up = True
        return ans
