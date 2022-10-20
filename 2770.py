while True:
    try:
        x, y, m = [int(i) for i in input().split()]
        while m:
            m -= 1
            a, b = [int(i) for i in input().split()]
            if (a <= x and b <= y) or (b <= x and a <= y):
                print("Sim")
            else:
                print("Nao")
    except EOFError:
        break
