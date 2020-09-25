while(True):

    try:

        dola = int(input())

        centavos = int(input())

        dolares = [ ]

        dola = str(dola)

        for j in range(len(dola)):

            dolares.append(dola[j])

        final = [ ]

        if(len(dolares) == 6):   

            i = 0

            while(i < len(dolares)):

                final.append(dolares[i])

                if(i == 2):

                    final.append(',')

                i = i + 1  

            if(centavos == 0):

                centavos = str(centavos)

                centavos = ".00" 

            elif(centavos > 0 and centavos < 9):

                centavos = "." + "0" + str(centavos)

            else:

                centavos = "." + str(centavos)

            mostra = ""  

            mostra = mostra.join(final) + centavos

            print("${}".format(mostra))

        elif(len(dolares) == 7):

            sete = dolares[0]

            i = 0

            dolares.remove(dolares[0])

            while(i < len(dolares)):

                final.append(dolares[i])

                if(i == 2):

                    final.append(',')

                i = i + 1 

            if(centavos == 0):

                centavos = str(centavos)

                centavos = ".00" 

            elif(centavos > 0 and centavos < 9):

                centavos = "." + "0" + str(centavos)

            else:

                centavos = "." + str(centavos)

            mostra = ""  

            mostra = sete + "," + mostra.join(final) + centavos

            print("${}".format(mostra))

        elif(len(dolares) == 8):

            sete = dolares[0]
            oito = dolares[1]

            i = 0

            dolares.remove(dolares[0])
            dolares.remove(dolares[1])

            while(i < len(dolares)):

                final.append(dolares[i])

                if(i == 2):

                    final.append(',')

                i = i + 1 

            if(centavos == 0):

                centavos = str(centavos)

                centavos = ".00" 

            elif(centavos > 0 and centavos < 9):

                centavos = "." + "0" + str(centavos)

            else:

                centavos = "." + str(centavos)

            mostra = ""  

            mostra = sete + oito + "," + mostra.join(final) + centavos

            print("${}".format(mostra))

        elif(len(dolares) == 9):

            sete = dolares[0]
            oito = dolares[1]
            nove = dolares[2]

            i = 0

            dolares.remove(dolares[0])
            dolares.remove(dolares[1])
            dolares.remove(dolares[2])

            while(i < len(dolares)):

                final.append(dolares[i])

                if(i == 2):

                    final.append(',')

                i = i + 1 

            if(centavos == 0):

                centavos = str(centavos)

                centavos = ".00" 

            elif(centavos > 0 and centavos < 9):

                centavos = "." + "0" + str(centavos)

            else:

                centavos = "." + str(centavos)

            mostra = ""  

            mostra = sete + oito + nove + "," + mostra.join(final) + centavos

            print("${}".format(mostra))

        elif(len(dolares) == 10):

            sete = dolares[3]
            oito = dolares[2]
            nove = dolares[1]
            dez  = dolares[0]

            i = 0

            dolares.remove(dolares[0])
            dolares.remove(dolares[1])
            dolares.remove(dolares[2])
            dolares.remove(dolares[3])

            while(i < len(dolares)):

                final.append(dolares[i])

                if(i == 2):

                    final.append(',')

                i = i + 1 

            if(centavos == 0):

                centavos = str(centavos)

                centavos = ".00" 

            elif(centavos > 0 and centavos < 9):

                centavos = "." + "0" + str(centavos)

            else:

                centavos = "." + str(centavos)

            mostra = ""  

            mostra = dez + "," + nove + oito + sete + "," + mostra.join(final) + centavos

            print("${}".format(mostra))


    except EOFError:

        break