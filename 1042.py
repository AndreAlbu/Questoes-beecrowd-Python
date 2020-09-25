n1, n2, n3 = input().split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

numeros = [n1, n2, n3]

numeros_ordem = numeros

numeros_ordem.sort()

print("{}\n{}\n{}\n".format(numeros_ordem[0], numeros_ordem[1], numeros_ordem[2]))
print("{}\n{}\n{}".format(n1, n2, n3))

