#3. По данному натуральному числу N найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!.
#Количество действий должно быть пропорционально N
def comp_sum(N):
    factorial=1
    s=0.1
    for i in range(1, N + 1):
        factorial *= i  
        s +=1/factorial  
    
    return s
N=int(input("Введите натуральное число N: "))
result=comp_sum(N)
print(f"{result:.5f}")
