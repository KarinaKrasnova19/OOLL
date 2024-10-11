#Вложенные списки 2
n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

new_matrix = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        new_matrix[j][n - 1 - i] = matrix[i][j]

for row in new_matrix:
    print(" ".join(map(str, row)))
