# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/2520
# Author: Álex Sousa Cruz (alequisk)

while True:
  try:
    N, M = list(map(int, input().split(" ")))
    xi, yi = 0, 0  # ash position
    xj, yj = 0, 0  # pokemon potision
    for i in range(N):
      line = list(map(int, input().split(' ')))
      if 1 in line:
        xi, yi = i, line.index(1)
      if 2 in line:
        xj, yj = i, line.index(2)
    
    print(abs(xi - xj) + abs(yi - yj))
  except EOFError:
    break