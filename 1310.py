# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1310
# Author: Álex Sousa Cruz (alequisk)

while True:
  try:
    N = int(input())
    cost = int(input())
    arr = [int(input()) for x in range(N)]
    answer = 0
    for i in range(N):
      acc = 0
      for j in range(i, N):
        acc += arr[j] - cost
        if answer < acc:
          answer = acc
    print(answer)
  except EOFError:
    break