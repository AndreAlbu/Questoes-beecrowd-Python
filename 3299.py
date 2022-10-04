numero = input("")

aux = numero

numero = list(numero)

i = 0
auxVeri = 0

while(i < len(numero) - 1):

	if(numero[i] == "1" and numero[i + 1] == "3"):

		auxVeri = 1
		break

	else:
		
		auxVeri = 0

		

	i = i + 1

if(auxVeri == 1):

	print("{} es de Mala Suerte".format(aux))

else:

	print("{} NO es de Mala Suerte".format(aux))