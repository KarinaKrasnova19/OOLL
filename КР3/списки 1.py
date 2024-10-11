#Вложенные списки 1
def snake(n, m):
    A = [[0] * m for _ in range(n)]

    num = 1 
    for i in range(n):
        if i % 2 == 0:  
            for j in range(m):
                A[i][j] = num
                num += 1
        else: 
            for j in range(m - 1, -1, -1):
                A[i][j] = num
                num += 1

    return A

def print_array(array):
    for row in array:
        print(' '.join(f"{num:2}" for num in row))

if __name__ == "__main__":
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
    
    snake_array = snake(n, m)
    print("Заполненный массив:")
    print_array(snake_array)







































    
