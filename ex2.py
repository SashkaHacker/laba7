#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == '__main__':
    lst = [float(s) for s in input().split()]
    # решение 1-ой задачи
    maxx = lst[1]
    for i in lst:
        if abs(i) > abs(maxx):
            maxx = i
    print(f"Номер максимального по модулю элемента списка: "
          f"{lst.index(maxx) + 1}")

    # решение 2-ой задачи
    summ = 0
    flag = False
    for i in lst:
        if flag:
            summ += i
        elif i >= 0:
            flag = True
    print(f"Сумма элементов списка, расположенных после 1-го"
          f" положительного числа: {summ}")

    # преобразование списка
    a, b = int(input("Введите а: ")), int(input("Введите b: "))
    new_lst = sorted(lst, key=lambda x: int(x) >= a <= b, reverse=True)
    print(new_lst)
