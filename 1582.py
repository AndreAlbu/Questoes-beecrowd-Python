# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1582
# Author: Alex Sousa Cruz (@alequisk)

import math

while True:
    try:
        arr = list(map(int, input().split()))
        arr.sort()
        [a, b, c] = arr
        if a ** 2 + b ** 2 == c ** 2:
            if math.gcd(a, b, c) == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break