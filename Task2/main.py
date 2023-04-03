# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

array = []
arr_len = int(input("Введите длину массива: "))

for i in range(arr_len):
    array.append(randint(0, 100))

print(*array)

number_to_find = int(input("Какое число в массиве вы хотите найти? "))
numbers_difference = number_to_find - array[0]
index_closest_number = 0

for i in range(len(array)):
    if number_to_find - i < numbers_difference:
        index_closest_number = i

print(f"Ближайшее число {array[index_closest_number]}")
