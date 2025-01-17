"""
Дано трехзначное число. Проверить истинность высказывания: Все цифры данного
числа различны """

# трехзначное число
number = 123

# Функции проверки неравенства
def CheckInequality(num):
    
    # делим на 100 на цело и получаем первое число (сотни)
    frstNum = number // 100
    # делим показывая остаток 0, потом делим на 10 на цело и получаем второе число (десятки)
    scndNum = (number % 100) // 10
    # аналогично. делим на 10, получаем остаток (десятки)
    thrdNum = number % 10
    
    if frstNum != scndNum and frstNum != thrdNum and scndNum != thrdNum:
        return True 
    
    return False

        
    # сработает если функция не возвращала Ложь, то вернет Истину
    return True

print(CheckInequality(number))