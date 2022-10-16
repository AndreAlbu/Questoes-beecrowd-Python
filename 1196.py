while True:
    try:
        teclado = "`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
        digita = input()
        for i in digita:
            if i==" ":
                print(" ", end="")
            else:
                print(teclado[teclado.index(i)-1], end="")
        print()
    except EOFError:
        break