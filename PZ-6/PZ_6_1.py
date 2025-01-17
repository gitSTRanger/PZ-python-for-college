'''
Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
элементов списка, кроме элементов с номерами от K до L включительно
'''
"""
import random

K = random.randint(2, 5)
L = random.randint(K, K+5)
N = random.randint(L,L+5)


numList = [int]

def WriteList(Flist_1: list[int] = int):
    for i in range(N):
        Flist_1.append(random.randint(0,N))
    return Flist_1


list = WriteList(numList)

def calculateSum(Flist_2):
    sum = 0
    firstPart = Flist_2[0:K-1]
    secondPart = Flist_2[L:-1]
    
    for elem in firstPart:
        sum += elem
    for elem in secondPart:
        sum += elem
    return sum
        



    

print(f'K:{K} L:{L} N:{N}')
print("сумма:", calculateSum(numList))
"""
