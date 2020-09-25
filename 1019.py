N = int(input())

horas = N / 3600

resto_segundo = N % 3600

minutos = resto_segundo / 60

segundo = resto_segundo % 60

print("{}:{}:{}".format(int(horas), int(minutos), int(segundo)))