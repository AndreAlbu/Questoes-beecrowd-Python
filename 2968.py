import math

l = input().split(" ")
v, n = l
total = int(v) * int(n)
p = 10.0
result = []
for i in range(1, 10):
  placa = (total * p)/100.0
  result.append(str(math.ceil(placa)))
  p += 10.0
saida = " ".join(result)
print(saida)