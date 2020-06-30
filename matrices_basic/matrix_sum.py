from matrix_gen import matrix_generator

def sum_matrices(matrixA, matrixB):
    '''It receives two matrices and retuns the sum between them.'''
    
    rows = len(matrixA)
    columns = len(matrixA[0])

    matrixC = matrix_generator(rows, columns, 0)

    for i in range(rows):
        for j in range(columns):
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
    
    return matrixC

if __name__ == '__main__':
    A = [[1,2,3], [4,5,6], [7,8,9]]
    B = [[10,20,30], [40,50,60], [70,80,90]]
    print(sum_matrices(A,B))
