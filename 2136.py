maior = ""
participante = []
participante_no = []

while(True):

    entrada = input("").split()

    candidato = entrada[0]

    if(candidato == "FIM"):

        break

    opcao = entrada[1]

    if(opcao == "YES"):

        if(len(candidato) > len(maior)):

            maior = candidato

        if(candidato not in participante):

            participante.append(candidato)

    else:

        participante_no.append(candidato)

participante.sort()
participante_no.sort()

for can in participante:

    print(can)

for can_no in participante_no:

    print(can_no)

print("\nAmigo do Habay:")
print(maior)