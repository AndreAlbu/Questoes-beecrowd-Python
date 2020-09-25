a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

quaB = b * b

delta = quaB - 4 * a * c

raizDelta = delta ** 0.5

a2 = 2 * a


if(a == 0.0 or delta < 0.0):

    print("Impossivel calcular")

else:

    raiz1 = ((- b + raizDelta) / a2)
    raiz2 = ((- b - raizDelta) / a2)

    print("R1 = {0:.5f}".format(raiz1))
    print("R2 = {0:.5f}".format(raiz2))
