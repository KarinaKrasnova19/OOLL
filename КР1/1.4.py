#4. Дано натуральное число N. Найдите количество нулей среди всех цифр числа N
N=input("Введите натуральное число N: ")
count_zero=0

for digit in N:
    if digit == '0':
        count_zero+=1
print(count_zero)
