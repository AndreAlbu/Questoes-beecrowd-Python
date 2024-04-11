anterior = 0
achou = -1

while True:
    try:
        valor = int(input(""))

        if anterior == 0:
            anterior = valor
        elif valor <= anterior or valor == anterior:
            anterior = valor
        else:
            if achou == -1:
                achou = valor + 1

    except EOFError:
        print(achou)
        break
