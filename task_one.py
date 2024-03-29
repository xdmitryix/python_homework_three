# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint
n = int(input('введи количество элементов массива: '))
k = int(input('введи число X: '))
numbers = [randint(1, n) for _ in range(n)]
print(numbers)
count = 0
for j in range(n):
    if numbers[j] == k:
        count += 1
if count == 0:
    print(f'число {k} не встречается в массиве')
else:
    print(f'число {k} встречается в массиве {count} раз(а)')


# Условие задачи очень странное. Сделал так, как будет логично для данной задачи.
# Элементы генерируются рандомом в диапазоне от 1 до n. Так логичнее.
# Иначе (судя по условию) число всегда будет встречаться 1 или 0 раз.