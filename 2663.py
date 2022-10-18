n = int(input())
k = int(input())
lista = []

for i in range(0, n):
    lista.append(int(input()))

def ordenacao_selecao(Lista):
    tamanho = len(Lista)
    
    for i in range(tamanho):
        maximo = i

        for j in range(i + 1, tamanho):
            if Lista[maximo] < Lista[j]:
                maximo = j

        Lista[i], Lista[maximo] = Lista[maximo], Lista[i]

ordenacao_selecao(lista)

finalistas = k
while finalistas < n and lista[finalistas] == lista[k-1]:
    finalistas += 1

print(finalistas)
