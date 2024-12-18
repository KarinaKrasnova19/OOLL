#2. По данному числу n вычислите сумму 1+1/2^2+1/3^2+...+1/n^2
def sum_of_squares(n):
    s=0
    for i in range(1,n+1):
        s+=1/(i**2)
    return s
n=int(input("Введите значение n: "))
result=sum_of_squares(n)
print(f"Сумма = {result}")
