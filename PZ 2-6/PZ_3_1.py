"""
Дано трехзначное число. Проверить истинность высказывания: Все цифры данного
числа различны """

# трехзначное число
number = 123

# Функции проверки неравенства
def CheckInequality(num):
    
    # Переводим число в строку
    strNumber = str(num)
    # поочередно проверяем каждое число на неравенство
    # *enumerate по мимо значениятекущей итерации, возвращает номер итерации(index_1, index_2)*
    for (index_1, num_1) in enumerate(strNumber):
         for (index_2, num_2) in enumerate(strNumber):
              # если число одно и то же, то пропустить итерацию до других чисел
              if index_1 == index_2:
                   continue
              # если две цифры одинаковы, то вернуть Ложь
              if num_1 == num_2:
                   return False
        
    # сработает если функция не возвращала Ложь, то вернет Истину
    return True

print(CheckInequality(number))