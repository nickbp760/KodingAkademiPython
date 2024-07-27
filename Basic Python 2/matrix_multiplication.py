def matrix_multiplication(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    matrix3 = []
    # Perform multiplication
    for i in range(rows_matrix1):
        rows = []
        for j in range(cols_matrix2):
            total = 0
            for k in range(cols_matrix1):
                total += matrix1[i][k] * matrix2[k][j]
            rows.append(total)
        matrix3.append(rows)

    return matrix3

# Example usage
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

result = matrix_multiplication(matrix1, matrix2)

print("Result of matrix multiplication:")
for row in result:
    print(row)
