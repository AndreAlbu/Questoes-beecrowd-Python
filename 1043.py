a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

soma1 = b + c
soma2 = a + b
soma3 = a + c

if(a < soma1 and b < soma3 and c < soma2):

    perimetro = a + b + c

    print("Perimetro = {0:.1f}".format(perimetro))

else:

    area = ((a + b) * c) / 2

    print("Area = {0:.1f}".format(area))