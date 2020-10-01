import math
#aceita ai meu pr

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

#Realiza os calculos#

calx = (x2 - x1) * (x2 - x1)
caly = (y2 - y1) * (y2 - y1)

distancia = (calx + caly) ** 0.5

print("{0:.4f}".format(distancia))
