from matrix_gen import matrix_generator
from matrix_sho import show_matrix

def multiplies_matrices(matrixA, matrixB):
    '''Receives two arrays and returns the product.'''

    rows = len(matrixA)
    columns = len(matrixB[0])
    matrixC = matrix_generator(rows, columns)

    for i in range(len(matrixC)):
        for j in range(len(matrixC[0])):
            matrixB_column = convert_column_to_list(matrixB,j)
            
            matrixC[i][j] = product_of_line(matrixA[i], matrixB_column)

    return matrixC

def product_of_line(rowA, columnB):
    '''Receives the row and column of the matrix to be multiplied.'''
    product = 0

    for i in range(len(rowA)):
        product += rowA[i] * columnB[i]
     
    return product

def convert_column_to_list(matrix, index):
    '''Convet a columm of a matriz to a list'''
    listTemp = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == index:
                listTemp.append(matrix[i][j])
    return listTemp


if __name__ == '__main__':
    A = [[2, 1, 4], [0, 1, 1]]
    B = [[6, 3, -1, 0], [1, 1, 0, 4], [-2, 5, 0, 2]]
    C = [[5, 27, -2, 12], [-1, 6, 0, 6]]

    print('A matriz "A" é:')
    show_matrix(A)

    print('#'*20)

    print('A matriz "B" é:')
    show_matrix(B)

    print('#'*20)

    print('Temos o seguinte resultado da multiplicação:')
    show_matrix(multiplies_matrices(A, B))
