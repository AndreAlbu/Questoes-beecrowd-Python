# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/2840
# Author: Alex Sousa Cruz (@alequisk)

pi = 3.1415
[r, l] = list(map(int, input().split()))
print(int(l // ((r ** 3) * pi * 4 / 3)))