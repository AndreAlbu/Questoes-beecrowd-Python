bolinhas = int(input(""))

galhos = int(input(""))

dif = round(galhos / 2)

if(bolinhas >= galhos or dif < bolinhas):

	print("Amelia tem todas bolinhas!")

elif(dif > bolinhas):

	difGalhos = round(galhos / 2)

	dif = difGalhos - bolinhas

	print("Faltam {} bolinha(s)".format(dif))

else:

	print("Amelia tem todas bolinhas!")
