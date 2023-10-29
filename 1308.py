# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1308
# Auhor: Alex Sousa Cruz (@alequisk)

def sm(n):
    return (1 + n) * n / 2


for _ in range(int(input())):
    n = int(input())
    hi = 1414213561
    lo = 0
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if sm(mid) <= n:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)
