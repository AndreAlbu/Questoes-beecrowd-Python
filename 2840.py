entrada = input("").split()

raio = int(entrada[0])
gas = int(entrada[1])

v = (4 / 3) * (3.1415 * raio**3)

print(int(gas / v))
