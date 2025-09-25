def print_matrix(matrix: float, rows: int, cols: int):
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j] + 0, end=" ")
        print()
        
rowsC = 0
colsC = 0
matrixC = []

print("Matrix A:")

rowsA = int(input("Rows: "))
colsA = int(input("Columns: "))

matrixA = [[0 for _ in range(colsA)] for _ in range(rowsA)]
        
for i in range(rowsA):
    for j in range(colsA):
        matrixA[i][j] = float(input(f"A({i}, {j}): "))

print("Matrix B:")

rowsB = int(input("Rows: "))
colsB = int(input("Columns: "))

matrixB = [[0 for _ in range(colsB)] for _ in range(rowsB)]
        
for i in range(rowsB):
    for j in range(colsB):
        matrixB[i][j] = float(input(f"A({i}, {j}): "))

op = int(input("Operation - Addition: 1, Scalar Multiplication(on matrix A): 2, Matrix Multiplication: 3 - "))


if op == 1: # addition
    
    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        raise ValueError("Both matrices must be of the same size m x n for addition")
    
    rowsC = rowsA
    colsC = colsB
    
    matrixC = [[0 for _ in range(colsC)] for _ in range(rowsC)]
    
    for i in range(rowsA):
        for j in range(colsA):
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
                
elif op == 2: # scalar multiplication
    
    c = int(input("Scalar: "))
    
    rowsC = rowsA
    colsC = colsA
    
    matrixC = [[0 for _ in range(colsC)] for _ in range(rowsC)]
    
    for i in range(rowsA):
        for j in range(colsA):
            matrixC[i][j] = matrixA[i][j] * c
                
else: # matrix multiplication
    
    if len(matrixA[0]) != len(matrixB):
        raise ValueError("# of columns in A must be equal to the # of rows in B")

    rowsC = len(matrixA)
    colsC = len(matrixB[0])
    
    matrixC = [[0 for _ in range(colsC)] for _ in range(rowsC)]

    for i in range(rowsC):
        for j in range(colsC):
            sum = 0
            for k in range(rowsA):
                sum += matrixA[i][k] * matrixB[k][j]
                
            print(i)
            matrixC[i][j] = sum
    

print("Matrix A: ")
print_matrix(matrixA, rowsA, colsA) 

print("Matrix B: ")
print_matrix(matrixB, rowsB, colsB) 

print("Output: ")
print_matrix(matrixC, rowsC, colsC) 