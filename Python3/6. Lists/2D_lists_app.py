matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1])

matrix[2][1] = 20
print(matrix)

# For loop in the 2D matrix
for row in matrix:
    for item in row:
        print(item)