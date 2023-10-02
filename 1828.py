def jogo(she, raj):

    if(she == raj):

        return 3
    
    else:

        if(she == "tesoura"):

            if(raj == "papel" or raj == "lagarto"):

                return 1
            
            else:

                return 2
            
        elif(she == "papel"):

            if(raj == "pedra" or raj == "Spock"):

                return 1
            
            else:

                return 2
            
        elif(she == "pedra"):

            if(raj == "lagarto" or raj == "tesoura"):

                return 1
            
            else:

                return 2
            
        elif(she == "lagarto"):

            if(raj == "papel" or raj == "Spock"):

                return 1
            
            else:

                return 2
            
        elif(she == "Spock"):

            if(raj == "tesoura" or raj == "pedra"):

                return 1
            
            else:

                return 2

qtdTestes = int(input(""))

for i in range(1, qtdTestes + 1):

    jogada = input("").split()

    sheldon = jogada[0]
    raj = jogada[1]

    resultado = jogo(sheldon, raj)

    if(resultado == 1):

        print("Caso #" + str(i) + ": Bazinga!")

    elif(resultado == 2):

        print("Caso #" + str(i) + ": Raj trapaceou!")

    else:

        print("Caso #" + str(i) + ": De novo!")
