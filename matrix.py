def matrix_multiply(A, B):
    # Check if matrices are compatible for multiplication
    if len(A[0]) != len(B):
        print("Matrices are not compatible for multiplication.")
        return None

    result = [[0] * len(B[0]) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage:
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = matrix_multiply(matrix_A, matrix_B)

if result_matrix:
    print("Matrix A:")
    for row in matrix_A:
        print(row)

    print("\nMatrix B:")
    for row in matrix_B:
        print(row)

    print("\nResult Matrix:")
    for row in result_matrix:
        print(row)
