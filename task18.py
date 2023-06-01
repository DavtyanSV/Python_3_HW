"""
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
"""
import random
n = int(input("Введите кол-во элементов в массиве -> "))
array = []
for i in range(n):
    x = random.randint(0,9)
    array.append(x)
print(array)

our_number = int(input("Введите цифру для нахождения ближайшего в массиве -> "))
output_number = 100000
min = 100000
"""
i = 0
while(i<len(array)):
    if abs(array[i]-our_number) < min:
        output_number=array[i]
        min = abs(array[i]-our_number)
    i+=1
"""
for i in range(len(array)):
    if abs(array[i]-our_number) < min:
        output_number=array[i]
        min = abs(array[i]-our_number)

print(output_number)
