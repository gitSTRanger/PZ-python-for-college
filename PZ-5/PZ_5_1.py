'''
Составить функцию, которая выполнит суммирования числового ряда
'''

# числовой ряд (список)
numberLine = [1,2,3,4,5]

# функция суммирования
def SumLineElements(list):
    # инициализация суммы
    sum = 0
    # цикл проходить по всему списку и суммирует каждый элемент
    for elem in list:
        sum += elem

    return sum

print(SumLineElements(numberLine))

