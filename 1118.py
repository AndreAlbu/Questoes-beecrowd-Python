# -*- coding: utf-8 -*-

nota_soma = 0 
cont = 0
continuar = True

while continuar==True:
  nota = float(input())
  
  if nota>=0.0 and nota <=10:
    nota_soma += nota
    cont += 1 

    if cont == 2:
      
      print("media = %.2f"%(nota_soma/2))
      cont = 0 
      nota_soma = 0

      while True:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())
        if novo == 2:
          continuar = False
          break
        elif novo == 1:
          continuar = True
          break
      
  else:
    print("nota invalida")
