salario = float(input())

if(salario > 0.00 and salario <= 2000.00):
    print('Isento')
elif(salario >= 2000.01 and salario <= 3000.00):
    faixa01 = 0.08 * (salario - 2000)
    print('R$ {:.2f}'.format(faixa01))
elif(salario >= 3000.01 and salario <= 4500.00):
    faixa01 = 0.08 * 1000
    faixa02 = 0.18 * (salario - 3000)
    print('R$ {:.2f}'.format(faixa01 + faixa02))
elif(salario > 4500.00):
    faixa01 = 0.08 * 1000
    faixa02 = 0.18 * 1500
    faixa03 = 0.28 * (salario - 4500)
    print('R$ {:.2f}'.format(faixa01 + faixa02 + faixa03))
