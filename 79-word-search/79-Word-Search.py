class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        u: dfs surrounding squares if we find match
        p:
            iterate board and check if find first letter
                dfs
                track the current letter of the word

                base case:
                    invalid r or c index
                    the square we dfs'd into is not a match
                iterative step:
                    match, continue surrounding dfs and increment to the next letter 
        '''
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] != word[i] or board[r][c] == '#':
                return

            temp = board[r][c]
            board[r][c] = '#'

            i += 1
            res = dfs(r+1, c,i) or dfs(r, c+1,i) or dfs(r-1, c, i) or dfs(r, c-1, i)

            board[r][c] = temp
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False