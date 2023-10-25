# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1459
# Author: Álex Sousa Cruz (alequisk)

while True:
  try:
    N = int(input())
    segments = []
    for i in range(N):
      x, y = list(map(int, input().split()))
      segments.append((y, x))
    
    segments.sort()
    answer = 0

    i = 0
    while i < N:
      answer += 1
      max_focus = segments[i][0]
      while i < N and segments[i][1] <= max_focus:
        i += 1  
    
    print(answer)
  except EOFError:
    break