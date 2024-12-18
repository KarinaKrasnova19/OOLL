#5. Выведите все точные квадраты натуральных чисел,
#не превосходящие данного числа N
N=int(input("Введите число N: "))
i=1
while True:
    square=i*i
    if square>N:
        break
    print(square)
    i+=1
