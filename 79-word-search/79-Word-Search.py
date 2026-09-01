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
        visited = set()

        def dfs(r, c, curr, i):
            if r >= rows or c >= cols or r < 0 or c < 0 or i >= len(word) or (r,c) in visited:
                return
            if board[r][c] != word[i]:
                return


            curr += board[r][c]
            visited.add((r,c))
            if curr == word:
                return True
            i += 1

            if dfs(r+1, c, curr,i) or dfs(r, c+1, curr,i) or dfs(r-1, c, curr,i) or dfs(r, c-1, curr,i):
                return True

            visited.remove((r,c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, "",0):
                    return True
        return False