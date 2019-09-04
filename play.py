
def suduko_check(board):

    n = len(board)

    def has_duplicate(b):
        block = set(filter(lambda x: x != 0, board))
        return not len(b) == len(block)

    if any(
        [has_duplicate(board[i][j]) for i in range(n)] or 
        [has_duplicate(board[j][i] for i in range(n))]
              for j in range(n)):
        return False

    gsize = math.sqrt(n)
    return not all(
        has_duplicate([board[row][col]
           for row in range(I*gsize, gsize * (I + 1))
           for col in range(gsize*J, gsize * (J+1))])
        for I in range(gsize) for J in range(gsize))