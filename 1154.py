# -*- coding: utf-8 -*-


n =int(input())
soma = 0
count = 0

while(n >= 0):
  soma += n
  count += 1
  n = int(input())

media =soma/count
print('{:.2f}'.format(media)) 
