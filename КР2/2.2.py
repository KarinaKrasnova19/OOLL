#1)Написать регулярное выражение, определяющее является ли данная строчка датой в формате dd/mm/yyyy. Начиная с 1600 года до 9999 года.
#– пример правильных выражений: 29/02/2000, 30/04/2003, 01/01/2003.
#– пример неправильных выражений: 29/02/2001, 30-04-2003, 1/1/1890
def date(date_str):
    if len(date_str)!=10 or date_str[2]!='/' or date_str[5]!='/':
        return False

    day=int(date_str[:2])
    month=int(date_str[3:5])
    year=int(date_str[6:])

    if year<1600 or year>9999:
        return False

    if month<1 or month>12:
        return False

    days_in_month = [31, 28 + (1 if (year%4==0 and (year%100!=0 or year%400==0)) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30,31]

    if day< 1 or day>days_in_month[month-1]:
        return False
    return True

print(date("29/02/2000"))
print(date("30/04/2003"))
print(date("01/01/2003"))
print(date("29/02/2001"))
print(date("30-04-2003"))
print(date("1/1/1890"))
