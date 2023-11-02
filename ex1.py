#!usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 11

if __name__ == "__main__":
    A = [int(input()) for _ in range(10)]
    count = []
    for i in A:
        if i < 0 and i % 7 == 0:
            count.append(i)

    print(f'Количество элементов:{len(count)}. Сумма элементов:{sum(count)}.')
