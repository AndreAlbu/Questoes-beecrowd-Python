# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/2884
# Author: Álex Sousa Cruz (alequisk)

N, M = list(map(int, input().split()))
lights = 0
turned_on = list(map(int, input().split()))
for i in range(1, len(turned_on)):
  lights |= 1 << turned_on[i]

interrupts = []

for s in range(N):
  values = list(map(int, input().split()))
  sequence = 0
  for i in range(1, len(values)):
    sequence |= 1 << values[i]
  interrupts.append(sequence)

have_answer = False
answer = 0

for test in range(0, N + N):
  position = test % N
  answer += 1
  lights ^= interrupts[position]
  if lights == 0:
    have_answer = True
    break
  
if have_answer:
  print(answer)
else:
  print(-1)