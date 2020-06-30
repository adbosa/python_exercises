def show_matrix(matrix_ref):
    ''' Print a readable matrix on the screen. '''
    rows = len(matrix_ref)
    columns = len(matrix_ref[0])
    for i in range(rows):
        for j in range(columns):
            if j < columns - 1:
                print(matrix_ref[i][j], end=' ')
            else:
                print(matrix_ref[i][j])
