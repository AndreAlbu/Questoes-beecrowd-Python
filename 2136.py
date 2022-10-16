inscritos_sim = []
inscritos_nao = []
amigo = ""
l = input().split()
while l[0] != 'FIM':
    if l[0] in inscritos_sim or l[0] in inscritos_nao:
        pass
    else:
        if l[1] == "YES":
            inscritos_sim.append(l[0])
            if len(l[0])>len(amigo):
                amigo = l[0]
        else:
            inscritos_nao.append(l[0])
    l = input().split()
inscritos_sim.sort()
inscritos_nao.sort()
inscritos = inscritos_sim+inscritos_nao
for i in inscritos:
    print(i)
print("\nAmigo do Habay:\n{}".format(amigo))


    