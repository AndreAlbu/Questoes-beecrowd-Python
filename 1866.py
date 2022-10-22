# -*- coding: utf-8 -*-

c = int(input())
lista = []
for i in range(0,c):
    j = int(input())
    s = 0
    for h in range(0, j):
        if h % 2 != 0:
            s -= 1
        if h % 2 == 0:
            s += 1
    lista += [s]
for l in range(0, c):
    print(f'{lista[l]}')
