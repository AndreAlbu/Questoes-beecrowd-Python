def meio(lista):

	listaAux = []

	maior = max(lista)
	menor = min(lista)

	listaAux = [menor, maior]

	for i in lista:
		
		if(i not in listaAux):

			ind = lista.index(i)
	
	return ind


h, z, l = input("").split()

h = int(h)
z = int(z)
l = int(l)

idades = [h, z, l]

meioIdades = meio(idades)

if(meioIdades == 0):

	print("huguinho")

elif(meioIdades == 1):

	print("zezinho")

else:

	print("luisinho")
