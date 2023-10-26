# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/2867
# Author: Álex Sousa Cruz (alequisk)

for _ in range(int(input())):
  n, m = list(map(int, input().split(" ")))
  v = str(n ** m)
  print(len(v))