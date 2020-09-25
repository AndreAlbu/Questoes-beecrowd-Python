alcool = 0
gasolina = 0
diesel = 0

while(1):

    tipo = int(input())

    if(tipo == 4):

        break

    elif(tipo > 4):

        tipo = 0
    
    else:

        if(tipo == 1):

            alcool = alcool + 1
        
        elif(tipo == 2):

            gasolina = gasolina + 1

        else:

            diesel = diesel + 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))