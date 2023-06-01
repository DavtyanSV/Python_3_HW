"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число 
"""
import random
n = int(input("Введите кол-во элементов в массиве -> "))
array = []
for i in range(n):
    x = random.randint(0,9)
    array.append(x)
print(array)
our_number = int(input("Введите цифру кол-во которого в массиве хотите узнать -> "))
count = 0
for i in range(len(array)-1):
    if our_number == array[i]:
        count+=1
print(count)