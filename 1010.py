codigo_1, quantidade_1, valor_1 = map(float, input().split())
codigo_2, quantidade_2, valor_2 = map(float, input().split())

resultado = (quantidade_1*valor_1)+(quantidade_2*valor_2)
print("VALOR A PAGAR: R$ %.2f" %round(resultado, 2))
