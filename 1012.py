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
print("Resultados abaixo")

#Resultados

print("TRIANGULO: {0:.3f}".format(triangulo))
print("CIRCULO: {0:.3f}".format(circulo))
print("TRAPEZIO: {0:.3f}".format(trapezio))
print("QUADRADO: {0:.3f}".format(quadrado))
print("RETANGULO: {0:.3f}".format(retangulo))
