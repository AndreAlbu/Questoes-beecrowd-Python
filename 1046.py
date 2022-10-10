i, t = input().split()
i = int(i)
t = int(t)
if i == t:
	h = 24
elif i <= t:
	h = t - i
else:
	h = (24-i)+t
print("O JOGO DUROU %d HORA(S)"%(h))
