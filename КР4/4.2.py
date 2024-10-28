#Вариант №4 (оценка 4)
#В проекте найдите класс BankAccount и унаследованные от него классы CardAccount и DepositAccount.
#Реализуйте методы классов, при необходимости переопределите методы в наследниках так, чтобы выполнялись условия пополнения и снятия:
#BankAccount — пополнение и списание происходит без комиссии. Если передать в метод пополнения отрицательное значение, сумма на счёте не должна измениться.
#При попытке снять большую сумму, чем есть на счёте, сумма не списывается со счёта, сумма на счёте не изменяется.
#CardAccount — карточный счёт, в дополнение к условиям BankAccount — при снятии денег должна взиматься комиссия 1% от суммы списания.
#Пример: при попытке снять со счёта 100 рублей должен списаться 101 рубль.
#DepositAccount — депозитный расчётный счёт, в дополнение к условиям BankAccount — нельзя снимать деньги в течение одного месяца после последнего пополнения.
#Переменную, в которой хранится дата последнего внесения, назовите lastIncome. Тип переменной используйте Calendar или LocalDate.

from datetime import datetime, timedelta

class BankAccount:
    def __init__(self,inital_balance=0):
        self.balance=inital_balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            
    def get_balance(self):
        return self.balance

    
class CardAccount(BankAccount):
    def withdraw(self,amount):
        total_amount=amount*1.01
        if total_amount<=self.balance:
            self.balance-=total_amount

            
class DepositAccount(BankAccount):
    def __init__(self,inital_balance=0):
        super().__init__(inital_balance)
        self.last_income=None
        
    def deposit(self,amount):
        super().deposit(amount)
        if amount>0:
            self.last_income=datetime.now()
            
    def withdraw(self,amount):
        if self.last_income and (datetime.now()<self.last_income+timedelta(days=30)):
            return
        super().withdraw(amount)
        
bank_account = BankAccount()
bank_account.deposit(100)
print("Баланс BankAccount:", bank_account.get_balance())

bank_account.withdraw(50)
print("Баланс BankAccount после снятия 50:", bank_account.get_balance())

card_account = CardAccount()
card_account.deposit(200)
print("Баланс CardAccount:", card_account.get_balance())

card_account.withdraw(100)
print("Баланс CardAccount после снятия 100:", card_account.get_balance())

deposit_account = DepositAccount()
deposit_account.deposit(300)
print("Баланс DepositAccount:", deposit_account.get_balance())

deposit_account.withdraw(100)
print("Баланс DepositAccount после снятия 100:", deposit_account.get_balance()) 

deposit_account.withdraw(50)
print("Баланс DepositAccount после снятия 50:", deposit_account.get_balance()) 


        
        
    
        
            
        
