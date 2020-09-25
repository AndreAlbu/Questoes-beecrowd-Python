import math

minutos = int(input())

while(minutos != 0):

    alemanha = 7 * minutos / 90

    alemanha = math.ceil(alemanha)

    brasil = minutos / 90

    brasil = math.floor(brasil)

    alemanha = int(alemanha)
    brasil = int(brasil)

    print("Brasil {} x Alemanha {}".format(brasil, alemanha))

    minutos = int(input())