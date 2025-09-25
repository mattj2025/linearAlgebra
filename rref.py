rows = int(input("Rows: "))
cols = int(input("Columns: "))

matrix = [[0 for _ in range(cols)] for _ in range(rows)]
pivots = [False for _ in range(rows)]
        
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"A({i}, {j}): "))

if input("Details(y/n): ") == "y":
    details = True
else:
    details = False

def print_matrix():
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j] + 0, end=" ")
        print()
        
# swaps two rows
def swap(r1: int, r2: int):
    temp = [0 for _ in range(cols)]
    
    for j in range(cols):
        temp[j] = matrix[r1][j]
        matrix[r1][j] = matrix[r2][j]
        matrix[r2][j] = temp[j]
        
# scales row r by a constant 'c'
def scale(r: int, c: float):
    for j in range(cols):
        matrix[r][j] *= c
        
# scales r1 by c and adds it to r2
def add(r1: int, r2: int, c: float):
    for j in range(cols):
        matrix[r2][j] += matrix[r1][j] * c

print("Input Matrix:")
print_matrix()


# search for first leading coefficient
#       scale row to get 1 as leading coefficient
#       swap if it's not in the first row
#       add to get rid of other coefficients in that col.

pivot = -1

for j in range(cols):
    for i in range(rows):
        
        if matrix[i][j] != 0:
            if not pivots[i]:
                if i != j:
                    if details:
                        print(f"Swapping rows {j} and {i}")
                    swap(j, i)
                    
                pivot = i
                if (matrix[i][j] != 1.0 and matrix[i][j] != 0):
                    c = 1 / matrix[i][j]
                    if details:
                        print(f"Scaling row {i} by {c}")
                    scale(i, c)
                    
                pivots[j] = True
                break
        
    for i in range(rows):
        
        if i != pivot and matrix[i][j] != 0 and matrix[pivot][j] != 0:
            c = - matrix[i][j] / matrix[pivot][j]
            if details:
                print(f"Adding row {pivot} * {c} to row {i}")
            add(pivot, i, c)
        

print("Reduced Matrix:")
print_matrix()