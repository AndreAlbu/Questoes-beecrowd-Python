# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/2544
# Author: Álex Sousa Cruz (alequisk)

while True:
  try:
    N = int(input())
    answer = 0
    qtd = 1
    while qtd < N:
      qtd *= 2
      answer += 1
    print(answer)
  except EOFError:
    break