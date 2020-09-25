data = int(input())

ano = data / 365

mes = (data % 365) / 30

dia = (data % 365) % 30

print("{} ano(s)".format(int(ano)))
print("{} mes(es)".format(int(mes)))
print("{} dia(s)".format(int(dia)))