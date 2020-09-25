otavio, bruno, ian = map(float, input().split())

if(otavio == bruno or otavio == ian or bruno == ian):

    print("Empate")

elif(otavio < bruno and otavio < ian):

    print("Otavio")

elif(bruno < otavio and bruno < ian):

    print("Bruno")

else:

    print("Ian")