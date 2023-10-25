# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1257
# Author: Álex Sousa Cruz (alequisk)

for testcase in range(int(input())):
  N = int(input())
  hashval = 0
  for element in range(N):
    s = input()
    for position in range(len(s)):
      hashval += element + position + ord(s[position]) - ord('A')
  print(hashval)