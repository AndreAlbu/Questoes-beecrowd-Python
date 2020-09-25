peças = int(input())

la, lb = map(int, input().split())
sa, sb = map(int, input().split())

if(peças >= la and peças <= lb and peças >= sa and peças <= sb):

    print("possivel")

else:

    print("impossivel")