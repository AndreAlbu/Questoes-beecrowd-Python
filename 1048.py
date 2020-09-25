salario = float(input())

if(salario >= 0.0 and salario <= 400.00):

    percentual = 0.15

    reajuste = salario * percentual

    novoSalario = salario + reajuste

elif(salario > 400.00 and salario <= 800.00):

    percentual = 0.12

    reajuste = salario * percentual

    novoSalario = salario + reajuste

elif(salario > 800.00 and salario <= 1200.00):

    percentual = 0.10

    reajuste = salario * percentual

    novoSalario = salario + reajuste

elif(salario > 1200.00 and salario <= 2000.00):

    percentual = 0.07

    reajuste = salario * percentual

    novoSalario = salario + reajuste

else:

    percentual = 0.04

    reajuste = salario * percentual

    novoSalario = salario + reajuste

percentual = percentual * 100

print("Novo salario: {0:.2f}".format(novoSalario))
print("Reajuste ganho: {0:.2f}".format(reajuste))
print("Em percentual: {} %".format(int(percentual)))