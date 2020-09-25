import math

n = int(input())

raiz5 = math.sqrt(5)

parte1 = ((1 + raiz5) / 2) ** n

parte2 = ((1 - raiz5) / 2) ** n

fibonacci =  (parte1 - parte2) / raiz5

print("{0:.1f}".format(fibonacci))