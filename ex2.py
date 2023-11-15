#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == '__main__':
    lst = [float(s) for s in input().split()]
    # решение 1-ой задачи
    abs_lst = [abs(i) for i in lst]
    maxx = max(abs_lst)
    print(f"Номер максимального по модулю элемента списка: "
          f"{abs_lst.index(maxx) + 1}")

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
    new_lst = sorted(lst, key=lambda x: int(x) <= a or int(x) >= b)
    print(new_lst)
