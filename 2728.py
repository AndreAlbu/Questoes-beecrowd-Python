# -*- coding: utf-8 -*-
entradas = []

while True:
    try:
        entradas.append(str(input()))        
    except EOFError:
        break

for line in entradas:
    a = b = c = d = e = False
    
    aux = line.split("-")

    if 'c' == aux[0][0].lower() or 'c' == aux[0][-1].lower():
        a = True
    if 'o' in aux[1][0].lower() or 'o' in aux[1][-1].lower():
        b = True
    if 'b' in aux[2][0].lower() or 'b' in aux[2][-1].lower():
        c = True
    if 'o' in aux[3][0].lower() or 'o' in aux[3][-1].lower():
        d = True
    if 'l' in aux[4][0].lower() or 'l' in aux[4][-1].lower():
        e = True

    if a and b and c and d and e:
        print("GRACE HOPPER")
    else:
        print("BUG")