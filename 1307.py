# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1307
# Author: Alex Sousa Cruz (@alequisk)

import math

for testcase in range(int(input())):
    s = int(input(), 2)
    t = int(input(), 2)

    if math.gcd(s, t) != 1:
        print(f"Pair #{testcase + 1}: All you need is love!")
    else:
        print(f"Pair #{testcase + 1}: Love is not all you need!")


