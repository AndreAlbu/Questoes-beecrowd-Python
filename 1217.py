total_gasto = 0
total_frutas = 0
n = int(input())
for i in range(n):
    total_gasto += float(input())
    frutas = len(input().split())
    total_frutas += frutas
    print("day {}: {} kg".format(i+1, frutas))
print("{:.2f} kg by day\nR$ {:.2f} by day".format(total_frutas/n, total_gasto/n))
