#coding:utf-8

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c) / 2

circulo = (c * c) * 3.14159

trapezio = ((a * c) / 2) + ((b * c) / 2)

quadrado = b * b

retangulo = a * b

#Exibe os resultados na tela#

print("TRIÂNGULO: {0:.3f}".format(triangulo))
print("CÍRCULO: {0:.3f}".format(circulo))
print("TRAPÉZIO: {0:.3f}".format(trapezio))
print("QUADRADO: {0:.3f}".format(quadrado))
print("RETÂNGULO: {0:.3f}".format(retangulo))
