'''
Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
элементов списка, кроме элементов с номерами от K до L включительно
'''

import random

K = random.randint(2, 5)
L = random.randint(K, (K+5))
N = random.randint(L,(L+5))


numList = []

def WriteList(Flist_1):
    for i in range(N +1):
        Flist_1.append(random.randint(0,N))
    return Flist_1


list = WriteList(numList)

def calculateSum(Flist_2):
    sum_ = 0
    firstPart = Flist_2[0:K]
    secondPart = Flist_2[L+1:]

    print(firstPart)
    print(secondPart)

    for elem in firstPart:
        sum_ += elem
    for elem in secondPart:
        sum_ += elem
    return sum_
        



    

print(f'K:{K} L:{L} N:{N}')
print(list)
print("сумма:", calculateSum(list))

