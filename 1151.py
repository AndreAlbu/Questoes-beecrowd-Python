n = int(input()) 

fibronaci = [0, 1]

for i in range(1, n+1):

    fib1 = fibronaci[-2]
    fib2 = fibronaci[-1]

    fibronaci.append(fib2 + fib1)

fibronaci = fibronaci[:-2]

fibronaci = str(fibronaci).replace(',', '')

print(fibronaci.strip("[]"))
