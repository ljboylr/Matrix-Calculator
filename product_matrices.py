def multiplying_matrices(matrixA, matrixB):
    rows_A = len(matrixA)
    columns_A = len(matrixA[0])
    rows_B = len(matrixB)
    columns_B = len(matrixB[0])

    if columns_A != rows_B:
        raise ValueError("Values mismatch")

    product_matrix = [[0 for _ in range(columns_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                matrixA[i][k] = int(matrixA[i][k])
                matrixB[k][j] = int(matrixB[k][j])
                product_matrix[i][j] += matrixA[i][k] * matrixB[k][j]

    return product_matrix
