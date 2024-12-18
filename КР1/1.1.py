#1. Найдите сумму последовательности натуральных чисел,
#если признаком окончания конца последовательности является два подряд идущих числа 0
def sum_natural_numb():
    total_sum=0
    zero_count=0

    while True:
        number=int(input("Введите число: "))
        if number==0:
            zero_count+=1
            if zero_count==2:
                break
        else:
            zero_count=0
            if number>0:
                total_sum+=number
    return total_sum

result=sum_natural_numb()
print("Сумма последовательности натуральных чисел:", result)
