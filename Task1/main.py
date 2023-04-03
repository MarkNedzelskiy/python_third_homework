# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5

# 1 2 3 4 5
# 3
# -> 1

from random import randint

array = []
arr_len = int(input("Введите длину массива: "))

for i in range(arr_len):
    array.append(randint(0, 10))

print(*array)

number_to_find = int(input("Какое число в массиве вы хотите найти? "))

number_count = {number_to_find: 0}

for item in array:
    if item == number_to_find:
        number_count[number_to_find] += 1

print(f"В массиве число {number_to_find} встречается {number_count[number_to_find]} раз(а).")